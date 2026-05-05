from django.shortcuts import render, redirect
from .models import Attendance
from apps.students.models import Student

# MARK ATTENDANCE
def mark_attendance(request):
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
def list_attendance(request):
    attendance = Attendance.objects.all()
    return render(request, "attendance/list.html", {"attendance": attendance})

def report(request, student_id):
    total = Attendance.objects.filter(student_id=student_id).count()
    present = Attendance.objects.filter(
        student_id=student_id,
        status="Present"
    ).count()

    percentage = 0
    if total > 0:
        percentage = (present / total) * 100

    return render(request, "attendance/report.html", {
        "total": total,
        "present": present,
        "percentage": percentage
    })