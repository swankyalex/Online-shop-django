from django.urls import path

from applications.generator import views

urlpatterns = [
    path("", views.home),
]
