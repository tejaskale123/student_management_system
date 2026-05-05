from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.decorators import login_required

# 🔐 ADD STUDENT
@login_required
def add_student(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    # ✅ allow both admin + teacher
    if not (is_admin(request.user) or is_teacher(request.user)):
        return render(request, 'error.html', {'message': 'Access Denied - Only Admin or Teacher can add students'})

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        class_id = request.POST.get("class_id")

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            class_id=class_id
        )

        return redirect("/students/list/")

    return render(request, "students/add.html")


# 🔐 LIST STUDENTS + SEARCH
@login_required
def list_students(request):
    query = request.GET.get("q")

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, "students/list.html", {"students": students})


# 🔐 DELETE STUDENT
@login_required
def delete_student(request, id):
    if not (request.user.is_superuser or is_admin(request.user)):
        return render(request, 'error.html', {'message': 'Access Denied - Only Admin can delete students'})
        
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect("/students/list/")


# 🔐 EDIT STUDENT
@login_required
def edit_student(request, id):
    is_admin_or_teacher = request.user.is_superuser or is_admin(request.user) or is_teacher(request.user)
    if not is_admin_or_teacher:
        return render(request, 'error.html', {'message': 'Access Denied - Only Admin or Teacher can edit students'})
        
    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.class_id = int(request.POST.get("class_id"))

        student.save()
        return redirect("/students/list/")

    return render(request, "students/edit.html", {"student": student})


def is_admin(user):
    return user.is_superuser or user.is_staff or user.groups.filter(name__iexact='Admin').exists()

def is_teacher(user):
    return user.groups.filter(name__iexact='Teacher').exists()

def is_student(user):
    return user.groups.filter(name__iexact='Student').exists()