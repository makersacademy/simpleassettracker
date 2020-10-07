from django.urls import path
from . import views


urlpatterns = [
    path('assets/', views.assets),
    path('assets/add', views.addAssets),
    path('usermanagement/unauthorized', views.unauthorizedUsers)
]
