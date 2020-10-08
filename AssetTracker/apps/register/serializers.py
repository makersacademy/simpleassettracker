from rest_framework import serializers
from .models import UnauthorizedUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ("id", "username", "email")

class UnauthorizedUserSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = UnauthorizedUser
    fields = ('id', 'user', 'company')

class ApproveUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('is_active',)


