from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
  Name = models.CharField(max_length=30)
  Owned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)