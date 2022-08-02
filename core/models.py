from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import *

# Create your models here.

USER = settings.AUTH_USER_MODEL

# The Abstract User class allows the school to leverage on django's auth system
# and still modify certain fields of choice 

class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    last_name = None
    first_name = None
    


    objects = CustomBaseManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []


class School (models.Model):

    CATEGORY = (
        ('PRY', 'Primary'),
        ('SEC', 'Secondary')
    )

    # The username should be the school reg. no.

    reg_number = models.CharField(unique=True, max_length= 50 )
    name = models.CharField(max_length=550)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    privacy_question = models.TextField(null= True , blank=True)
    secret_answer = models.TextField(null= True , blank=True)
    LGA = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to = 'school', default = 'default.jpg')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(USER, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name 

# This is the profile for each school (logo, location, dates)
class Parent (models.Model):

    fname = models.CharField(max_length= 255)
    lname = models.CharField(max_length= 255)
    user = models.OneToOneField(USER, on_delete=models.CASCADE)

    