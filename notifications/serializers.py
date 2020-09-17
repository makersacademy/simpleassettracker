from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("Type", "Title", "Body", "Time_Created", "Company", "Admin_Only", "Action_Required")