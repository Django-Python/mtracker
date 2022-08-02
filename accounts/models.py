
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):

    username = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    empid = models.CharField(max_length=8)
    designation = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
# Create your models here.
