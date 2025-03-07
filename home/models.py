from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    is_creator = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # Added description field
    profile_visibility = models.BooleanField(default=True)  # Added profile visibility field
    subscription_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    email= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username=models.CharField(max_length=30,unique=True)
    #sets time only when created
    date_joined=models.DateTimeField(verbose_name="joined_date" , auto_now_add=True)