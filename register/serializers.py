from rest_framework import serializers
from .models import UnauthorizedUser
from django.contrib.auth.models import User

class UnauthorizedUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UnauthorizedUser
    fields = ('User', 'Company')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ("username", "email")