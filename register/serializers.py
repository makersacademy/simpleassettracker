from rest_framework import serializers
from .models import UnauthorizedUser

class UnauthorizedUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UnauthorizedUser
    fields = ('User', 'Company')