from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('assets/api/asset/', views.AssetListCreate.as_view()),
	path('assets/api/asset/<int:pk>/', views.AssetDetail.as_view()),
]
