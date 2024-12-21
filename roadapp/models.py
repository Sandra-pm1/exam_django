from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=10,unique=True)

class Violation(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="images",null=True,blank=True)
    added_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle