from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Attendance
from apps.students.models import Student


# =========================
# ROLE CHECKS
# =========================

def is_admin(user):
    return (
        user.is_superuser
        or user.is_staff
        or user.groups.filter(name__iexact='Admin').exists()
    )


def is_teacher(user):
    return user.groups.filter(name__iexact='Teacher').exists()


# =========================
# MARK ATTENDANCE
# =========================

@login_required
def mark_attendance(request):

    # Permission Check
    if not (is_admin(request.user) or is_teacher(request.user)):
        return render(request, 'error.html', {
            'message': 'Access Denied - Only Admin or Teacher can mark attendance'
        })

    # Get all students
    students = Student.objects.all()

    # POST Request
    if request.method == "POST":

        student_id = request.POST.get("student_id")
        date = request.POST.get("date")
        status = request.POST.get("status")

        # Validation
        if not student_id or not date or not status:

            return render(request, "attendance/add.html", {
                "students": students,
                "error": "All fields are required"
            })

        # Get Student Object
        student = None
        for s in Student.objects.all():
            if str(s.pk) == str(student_id):
                student = s
                break

        if not student:
            return render(request, "attendance/add.html", {
                "students": students,
                "error": "Selected student not found"
            })

        # Prevent Duplicate Attendance
        already_marked = Attendance.objects.filter(
            student=student,
            date=date
        ).exists()

        if already_marked:

            return render(request, "attendance/add.html", {
                "students": students,
                "error": "Attendance already marked for this student today"
            })

        # Save Attendance
        Attendance.objects.create(
            student=student,
            date=date,
            status=status
        )

        messages.success(request, "Attendance marked successfully")

        return redirect("/attendance/list/")

    return render(request, "attendance/add.html", {
        "students": students
    })


# =========================
# LIST ATTENDANCE
# =========================

@login_required
def list_attendance(request):

    attendance = Attendance.objects.all().order_by('-date')

    return render(request, "attendance/list.html", {
        "attendance": attendance
    })


# =========================
# REPORT SUMMARY
# =========================

@login_required
def report_summary(request):

    total = Attendance.objects.count()

    present = Attendance.objects.filter(
        status="Present"
    ).count()

    absent = Attendance.objects.filter(
        status="Absent"
    ).count()

    percentage = 0

    if total > 0:
        percentage = (present / total) * 100

    return render(request, "attendance/report.html", {
        "total": total,
        "present": present,
        "absent": absent,
        "percentage": round(percentage, 2)
    })


# =========================
# STUDENT REPORT
# =========================

@login_required
def report(request, student_id):

    # Get student object
    student = None
    for s in Student.objects.all():
        if str(s.pk) == str(student_id):
            student = s
            break

    if not student:
        return redirect("/attendance/list/")

    # Total attendance
    total = Attendance.objects.filter(
        student=student
    ).count()

    # Present count
    present = Attendance.objects.filter(
        student=student,
        status="Present"
    ).count()

    # Absent count
    absent = Attendance.objects.filter(
        student=student,
        status="Absent"
    ).count()

    # Percentage
    percentage = 0

    if total > 0:
        percentage = (present / total) * 100

    return render(request, "attendance/report.html", {
        "student": student,
        "total": total,
        "present": present,
        "absent": absent,
        "percentage": round(percentage, 2)
    })