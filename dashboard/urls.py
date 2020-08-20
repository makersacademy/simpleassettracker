from django.urls import path

from .views import dashboardPageView

urlpatterns = [
    path('dashboard', dashboardPageView, name='home')
]
