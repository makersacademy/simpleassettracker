from django.urls import path
from . import views


urlpatterns = [
    path('assets/', views.assets ),
]