from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200, default="")
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    

    def __str__(self):
        return self.id , self.title


# class CustomUser(AbstractUser):
#     email = models.EmailField(null=True, unique=True)
#     username = models.CharField(max_length=50, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['username']