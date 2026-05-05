from django.shortcuts import render
from apps.students.models import Student
from apps.classes.models import Class
from apps.attendance.models import Attendance


def dashboard(request):
    total_students = Student.objects.count()
    total_classes = Class.objects.count()
    total_attendance = Attendance.objects.count()
    return render(request, "dashboard.html", {
        "total_students": total_students,
        "total_classes": total_classes,
        "total_attendance": total_attendance
    })
