from email import message
from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    remarks = models.TextField()

    def __str__(self):
        return self.name
