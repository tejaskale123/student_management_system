from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_class),
    path("list/", views.list_classes),
]