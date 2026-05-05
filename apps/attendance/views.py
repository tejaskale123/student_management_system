from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from apps.students.models import Student

def is_admin(user):
    return user.is_superuser or user.is_staff or user.groups.filter(name__iexact='Admin').exists()

def is_teacher(user):
    return user.groups.filter(name__iexact='Teacher').exists()

# MARK ATTENDANCE
@login_required
def mark_attendance(request):
    if not (is_admin(request.user) or is_teacher(request.user)):
        return render(request, 'error.html', {'message': 'Access Denied - Only Admin or Teacher can mark attendance'})
    
    students = Student.objects.all()

    if request.method == "POST":

        student_id = request.POST.get("student_id")
        date = request.POST.get("date")
        status = request.POST.get("status")

        print("student_id:", student_id)

        if not student_id or student_id == "None":
            return render(request, "attendance/add.html", {
                "students": students,
                "error": "Invalid student selected. Please create a new student record."
            })

        Attendance.objects.create(
            student_id=student_id,
            date=date,
            status=status
        )

        return redirect("/attendance/list/")

    return render(request, "attendance/add.html", {"students": students})


# LIST ATTENDANCE
@login_required
def list_attendance(request):
    attendance = Attendance.objects.all()
    return render(request, "attendance/list.html", {"attendance": attendance})

@login_required
def report_summary(request):
    total = Attendance.objects.count()
    present = Attendance.objects.filter(status="Present").count()
    absent = Attendance.objects.filter(status="Absent").count()
    percentage = 0
    if total > 0:
        percentage = (present / total) * 100

    return render(request, "attendance/report.html", {
        "total": total,
        "present": present,
        "absent": absent,
        "percentage": percentage
    })

@login_required
def report(request, student_id):
    total = Attendance.objects.filter(student_id=student_id).count()
    present = Attendance.objects.filter(
        student_id=student_id,
        status="Present"
    ).count()
    absent = Attendance.objects.filter(
        student_id=student_id,
        status="Absent"
    ).count()

    percentage = 0
    if total > 0:
        percentage = (present / total) * 100

    return render(request, "attendance/report.html", {
        "total": total,
        "present": present,
        "absent": absent,
        "percentage": percentage
    })