from django.db import models
from django.contrib.auth.models import User
from companies.models import Company
from django.db.models.signals import post_save
from django.dispatch import receiver

class CompanyUser(models.Model):
  User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
  Company = models.ForeignKey(Company, on_delete=models.CASCADE)
