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

def login_view(request):
    from django.contrib.auth import authenticate, login
    from django.shortcuts import render, redirect
    
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('/students/list/')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
            
    return render(request, "login.html")

def logout_view(request):
    from django.contrib.auth import logout
    from django.shortcuts import redirect
    logout(request)
    return redirect('/login/')
