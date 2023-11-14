from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)



class Todo(models.Model):
    name=models.CharField(max_length=100, default="", null=True)
    description=models.CharField(max_length=500, default="", null=True)

