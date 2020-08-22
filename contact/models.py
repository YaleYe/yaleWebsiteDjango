from django.db import models
from django.utils import timezone
# Create your models here.

class contactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=15)