from django.urls import path

from .views import show_assets

urlpatterns = [
    path('', show_assets, name='assets')
]