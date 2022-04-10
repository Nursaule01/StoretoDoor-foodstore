from django.db import models


# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)


class User(models.Model):
    fullName = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return {
            'fullName': self.fullName,
            'email': self.email,
            'phoneNumber': self.phoneNumber,
            'gender': self.gender,
            'password': self.password,
            'address': self.address,
        }
