from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        verbose_name="id"
    )
    firstname = models.CharField(
        max_length=100,
        verbose_name="first_name"
    )
    lastname = models.CharField(
        max_length=100,
        verbose_name="last_name"
    )
    age = models.IntegerField(
        verbose_name="age"
    )
    address = models.CharField(
        max_length=100,
        verbose_name="address"
    )
    position = models.CharField(
        max_length=100,
        verbose_name="position"
    )
    username = models.EmailField(
        verbose_name="username"
    )
    password = models.CharField(
        max_length=100,
        verbose_name="password"
    )



class Images(models.Model):
    images = models.FileField(upload_to='profilepic',max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

