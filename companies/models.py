from django.db import models

# Create your models here.
class Company(models.Model):
  Name = models.CharField(max_length=30)