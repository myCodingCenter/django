from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role_choices = [
        ('student','Student'),
        ('teacher','Teacher')
    ]
    role = models.CharField(max_length=10,choices=role_choices,default='student')

    def __str__(self):
        return self.user.username+self.role + "'s profile"