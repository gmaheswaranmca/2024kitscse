from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length = 255)
    ratings = models.IntegerField(default=1)
    place = models.CharField(max_length=255,default='')
    phone_number = models.CharField(max_length=20,default='')

