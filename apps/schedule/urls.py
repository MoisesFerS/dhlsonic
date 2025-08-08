# ==================================================
# IMPORTS
# ==================================================

from django.urls import path
from . import views

# ==================================================
# ROUTES
# ==================================================

# App Name
app_name = 'schedule'

# URL Patterns
urlpatterns = [

    # Index page
    path('', views.index, name="index")

]
