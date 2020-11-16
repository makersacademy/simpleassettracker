from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=30, unique=True)
	owned_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
