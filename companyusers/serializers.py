from rest_framework import serializers
from .models import CompanyUser

class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = ('User', 'Company')