from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length= 255)
    created_at = models.DateField(auto_now=True)
    email = models.EmailField(max_length=254,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def get_username(self):
        return self.email
    def __str__(self):
        return self.email
