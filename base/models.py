from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=3000)
    price = models.FloatField()
    stock = models.IntegerField()
