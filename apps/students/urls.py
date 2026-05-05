from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_student),
    path("list/", views.list_students),
    path("delete/<str:id>/", views.delete_student),
    path("edit/<str:id>/", views.edit_student),
]