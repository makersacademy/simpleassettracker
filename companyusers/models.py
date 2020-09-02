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

@receiver(post_save, sender=User)
def create_companyuser(sender, instance, created, **kwargs):
    if created:
        C = CompanyUser.objects.create(User=instance, Company=Company.objects.get(Name="Makers"))
        C.save()
