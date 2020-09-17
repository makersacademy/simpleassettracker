from django.urls import path
from . import views

urlpatterns = [
  path('notifications/api/notifications/', views.NotificationList.as_view()),
]