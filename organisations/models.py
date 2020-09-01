from django.db import models

# Create your models here.
class Organisation(models.Model):
  name = models.CharField(max_length=30)