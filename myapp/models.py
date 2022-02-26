from django.db import models

# Create your models here.
class contect(models.model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField()