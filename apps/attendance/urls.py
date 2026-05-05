from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.mark_attendance),
    path("list/", views.list_attendance),
    path("report/<int:student_id>/", views.attendance_report),
]