from django.db import models

#https://docs.djangoproject.com/en/3.0/ref/models/fields/
# Create your models here.
class product(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(blank = True, null=True)
    price       = models.FloatField()
    summary     = models.TextField(default="quick summary")
