# Generated by Django 4.0.3 on 2022-03-31 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.address')),
            ],
        ),
    ]
