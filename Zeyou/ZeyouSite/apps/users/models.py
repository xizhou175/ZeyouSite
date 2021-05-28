from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# four departments: a:小助手  b:文案   c:顾问   d:助教
class User(AbstractUser):
    username = models.CharField(max_length=64, db_index=True, unique=True)
    phone = models.CharField(max_length=64, db_index=True, unique=True)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=128)
    department = models.CharField(max_length=128)

    #student = models.ManyToManyField(to='Student')
    #academy = models.ManyToManyField(to='Academy')

    def __str__(self):
        return '<User {}>'.format(self.username)
