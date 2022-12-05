from django.db import models

# Create your models here.

class Dates(models.Model):
    Name=models.CharField(max_length=20,default="")
    City=models.CharField(max_length=10,default="")
    Email=models.CharField(max_length=20,default="")
    Contect=models.CharField(max_length=10,default="")
