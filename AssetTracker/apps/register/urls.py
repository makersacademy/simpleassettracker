from django.urls import path
from . import views

urlpatterns = [
    path("registercompany/", views.register_company, name="registercompany"),
    path("registeruser/", views.register_user, name="registeruser"),
    path('preregister/', views.pre_register_view, name="preregister"),
    path('unauthorizedusers/api/unauthorizedusers', views.UnauthorizedUserList.as_view()),
    path('unauthorizedusers/api/unauthorizedusers/<int:pk>/', views.UnauthorizedUserDelete.as_view()),
    path('approveuser/api/approveuser/<int:pk>/', views.ApproveUser.as_view()),
]
