from django.urls import path

from .views import dashboard_page_view

# pylint: disable=bad-continuation
# pylint: disable=invalid-name
urlpatterns = [
    path('dashboard', dashboard_page_view, name='home')
]
