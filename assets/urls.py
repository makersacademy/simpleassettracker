from django.urls import path
from . import views

urlpatterns = [
    path('assets/api/asset/', views.AssetListCreate.as_view() ),
]