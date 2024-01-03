from django.db import models

# Create your models here.

class students(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField(max_length=40)