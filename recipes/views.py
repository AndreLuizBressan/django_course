"""
Module responsible for storing recipes-related
views definitions
"""

from django.shortcuts import render


# Create your views here.
def home(request):
    """
    View responsible for rendering the home page html
    """
    return render(request=request,
                  template_name='recipes/pages/home.html',
                  )
