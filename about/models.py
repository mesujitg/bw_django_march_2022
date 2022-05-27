from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.BooleanField(default=True)


class User(AbstractUser):
    type = models.CharField(max_length=255)
