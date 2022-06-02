from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=255, default='')
    is_viewer = models.BooleanField(default=True)

