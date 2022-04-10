import json
from pprint import pprint

from django.shortcuts import render, redirect

# Create your views here.
from main.models import Address, User


def index(req):
    if not req.session.get('user'):
        return redirect('/authorize')
    userId = req.session.get('user')

    user = User.objects.get(id=int(userId))

    return render(req, 'index.html', {
        'user': user
    })


def authorize(request):
    return render(request, 'authorize.html')


def product(req):
    return render(req, 'product.html')


def login(req):
    if req.method == 'POST':
        username = req.POST['email']
        password = req.POST['pass']

        errors = []
        try:
            user = User.objects.get(email=username, password=password)
            if user is None:
                errors.append('Invalid login or password')

            req.session['user'] = user.id
            return redirect('/', req)

        except User.DoesNotExist:
            errors.append('No users registered')

        if len(errors):
            return render(req, 'authorize.html', {
                'errors': errors
            })

        return render(req, 'authorize.html')

def logout(req):
    del req.session['user']

    return redirect('/authorize')


def register(req):
    if req.method == 'POST':
        # address
        country = req.POST["country"]
        city = req.POST['city']
        street = req.POST['street']
        house = req.POST['house']

        address = Address(
            country=country,
            city=city,
            street=street,
            house=house
        )
        address.save()

        # user
        email = req.POST['email']
        phone = req.POST['phone']
        password = req.POST['pass']
        password2 = req.POST['pass2']

        errors = []

        duplicateUser = User.objects.filter(email=email)
        duplicateNumber = User.objects.filter(phoneNumber=phone)

        if len(duplicateUser):
            errors.append('Email must be unique')

        if len(duplicateNumber):
            errors.append('Number must be unique')

        if password != password2:
            errors.append('Passwords does not match')

        if len(errors):
            return render(req, 'authorize.html', {
                'errors': errors
            })

        name = req.POST['name']
        gender = req.POST['gender']
        new_user = User(
            fullName=name,
            email=email,
            phoneNumber=phone,
            gender=gender,
            password=password,
            address_id=address.id
        )
        new_user.save()

        req.session['user'] = new_user.id

        return redirect('/', req)
        # return render()
