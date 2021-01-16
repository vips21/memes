from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    accept_cookie = models.NullBooleanField(null=True, blank=True)