from django.urls import path
from . import views


urlpatterns = [
    path('assets/', views.assets),
    path('assets/add', views.add_assets),
    path('usermanagement/unauthorized', views.unauthorized_users),
    path('import/', views.importcsv)
]
