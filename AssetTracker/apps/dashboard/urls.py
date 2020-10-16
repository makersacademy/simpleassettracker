from django.urls import path

from .views import dashboardPageView

# pylint: disable=bad-continuation
# pylint: disable=invalid-name
urlpatterns = [
    path('dashboard', dashboardPageView, name='home')
]
