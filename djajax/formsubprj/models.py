from django.db import models

# Create your models here.
class user_profile(models.Model):
    user_name = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=12)
    
    def __str__(self):
        return self.user_name