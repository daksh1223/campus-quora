from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=30)
    hostel = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    def __str__ (self):
        return self.email