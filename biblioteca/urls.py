from django.urls import path

from biblioteca.views import home

urlpatterns = [
    path("", home)
]