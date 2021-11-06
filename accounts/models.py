from django.db import models

# Create your models here.

class Profile(models.Model):
    email = models.EmailField(blank=True, default="")
    
    def __str__(self):
        return self.email
    
class User(models.Model):
    login = models.CharField(blank=True, max_length=12, default="user")
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.login
    

