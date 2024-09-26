from django.urls import path
from lenDjango import views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]