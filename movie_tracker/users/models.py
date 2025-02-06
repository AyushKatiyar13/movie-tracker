from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's built-in AbstractUser.
    This allows future modifications like adding more fields.
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
