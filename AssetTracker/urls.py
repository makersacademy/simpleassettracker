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
from django.conf.urls import url
from django.contrib import admin, auth
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AssetTracker.apps.index.urls')),
    path('', include('AssetTracker.apps.dashboard.urls')),
    path('', include('AssetTracker.apps.assets.urls')),
    path('', include('AssetTracker.apps.companyusers.urls')),
    path('', include('AssetTracker.apps.register.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include('AssetTracker.apps.reactfrontend.urls')),
    url('^', include('django.contrib.auth.urls')),
]
