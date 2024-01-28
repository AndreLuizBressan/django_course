"""
Module responsible for storing recipes-related
url routing definition
"""

from django.urls import path

from .views import home


urlpatterns = [
    path('', home)
]
