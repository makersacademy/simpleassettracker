from django.urls import path
from . import views

urlpatterns = [
    path('preregister/', views.preregisterview, name="preregister"),
]
