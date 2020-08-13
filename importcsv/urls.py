from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
  path('import/', views.importView, name="import"),
  url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
]
