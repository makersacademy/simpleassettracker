from django.urls import path
from . import views

urlpatterns = [
    path('api/asset/', views.AssetListCreate.as_view() ),
]