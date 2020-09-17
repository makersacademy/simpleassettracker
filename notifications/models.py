from django.db import models
from companies.models import Company

# Create your models here.

class Notification(models.Model):
  Type = models.CharField(max_length=30)
  Title = models.CharField(max_length=40)
  Body = models.CharField(max_length=300)
  Time_Created = models.DateTimeField(auto_now_add=True)
  Company = models.ForeignKey(Company, on_delete=models.CASCADE)
  Admin_Only = models.BooleanField(default=False)
  Action_Required = models.BooleanField(default=False)
