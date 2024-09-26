from django.urls import path
from lenDjango import views

urlpatterns = [
    path("", views.home, name="home"),
]