"""
URL configuration for dhlsonic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# ==================================================
# IMPORTS
# ==================================================

from django.contrib import admin
from django.urls import path, include

# ==================================================
# ROUTES
# ==================================================

urlpatterns = [

    # Index page(redirects to core app)
    path('', include('apps.core.urls')),

    # Schedule page(redirects to schedule app)
    path('schedule/', include('apps.schedule.urls')),

]
