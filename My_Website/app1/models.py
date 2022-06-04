from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=30,null=False)
    msg = models.TextField(max_length=100)
