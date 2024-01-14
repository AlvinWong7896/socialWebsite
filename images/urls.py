from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path("image/create/", views.image_create, name="create"),
]
