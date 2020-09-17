"""AssetTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import include, path
from register import views as v

urlpatterns = [
    path('', include('index.urls')),
    path('', include('dashboard.urls')),
    path('', include('assets.urls')),
    path('', include('companyusers.urls')),
    path('', include('register.urls')),
    path('admin/', admin.site.urls),
    path("registercompany/", v.registercompany, name="registercompany"),
    path("registeruser/", v.registeruser, name="registeruser"),
    path('', include("django.contrib.auth.urls")),
    path('', include('reactfrontend.urls')),
    path('', include('importcsv.urls')),
]
