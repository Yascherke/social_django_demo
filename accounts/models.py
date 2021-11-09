from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=35, blank=True, default="user")
    email = models.EmailField(blank=True, default="")
    password = models.CharField(max_length=50, blank=True , default="none")
    
    def __str__(self):
        return self.name
