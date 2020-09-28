from django.urls import path
from . import views

urlpatterns = [
  path('companyusers/api/companyusers/all', views.CompanyUserListCreate.as_view()),
  path('companyusers/api/companyusers/', views.CompanyUserList.as_view()),
  path('companyusers/api/companyusers/<int:pk>/', views.CompanyUserDetail.as_view()),
]