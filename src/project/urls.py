from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("generator/", include("generator.urls")),
    path("", include("products.urls")),
]
