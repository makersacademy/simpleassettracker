from django.urls import path

from .views import homePageView

urlpatterns = [
    path('dashboard', homePageView, name='home')
]
