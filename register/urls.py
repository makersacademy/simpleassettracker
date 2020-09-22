from django.urls import path
from . import views

urlpatterns = [
    path('preregister/', views.preregisterview, name="preregister"),
    path('unauthorizedusers/api/unauthorizedusers', views.UnauthorizedUserList.as_view()),
]