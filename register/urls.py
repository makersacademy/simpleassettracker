from django.urls import path
from . import views

urlpatterns = [
    path('preregister/', views.preregisterview, name="preregister"),
    path('password_reset/', views.passwordresetview, name="password_reset"),
]