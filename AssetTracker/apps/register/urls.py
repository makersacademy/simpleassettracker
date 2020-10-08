from django.urls import path
from . import views

urlpatterns = [
    path("registercompany/", views.registercompany, name="registercompany"),
    path("registeruser/", views.registeruser, name="registeruser"),
    path('preregister/', views.preregisterview, name="preregister"),
    path('unauthorizedusers/api/unauthorizedusers', views.UnauthorizedUserList.as_view()),
    path('unauthorizedusers/api/unauthorizedusers/<int:pk>/', views.UnauthorizedUserDelete.as_view()),
    path('approveuser/api/approveuser/<int:pk>/', views.ApproveUser.as_view()),
]
