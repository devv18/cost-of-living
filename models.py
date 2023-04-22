from django.db import models

# Create your models here.
class data(models.Model):
    c=models.CharField(max_length=100)
    t=models.CharField(max_length=100)
    links=models.CharField(max_length=100)


