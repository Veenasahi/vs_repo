from django.db import models
# Create your models here.
from django.db import models
# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=120)
    title=models.CharField(max_length=150)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class BngJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=120)
    title=models.CharField(max_length=150)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=120)
    title=models.CharField(max_length=150)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

