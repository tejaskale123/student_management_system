from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Student
from apps.classes.models import Class
from utils.permissions import is_admin, is_teacher

# 🔐 ADD STUDENT
@login_required
def add_student(request):

    if not (is_admin(request.user) or is_teacher(request.user)):
        return render(request, 'error.html', {
            'message': 'Access Denied - Only Admin or Teacher can add students'
        })

    raw_classes = Class.objects.all()

    classes = []

    for c in raw_classes:
        classes.append({
            "mongo_id": str(c.pk),
            "class_name": c.class_name,
            "section": c.section
        })

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        class_id = request.POST.get("class_id")

        student_class = None

        for c in Class.objects.all():
            if str(c._id) == str(class_id):
                student_class = c
                break

        if not student_class:
            return render(request, "students/add.html", {
                "classes": classes,
                "error": "Selected class not found"
            })

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            student_class=student_class
        )

        return redirect("/students/list/")

    return render(request, "students/add.html", {
        "classes": classes
    })


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
        
    student = None
    for s in Student.objects.all():
        if str(s._id) == str(id):
            student = s
            break
            
    if not student:
        from django.http import Http404
        raise Http404("No Student matches the given query.")

    student.delete()
    return redirect("/students/list/")


# 🔐 EDIT STUDENT
@login_required
def edit_student(request, id):
    is_admin_or_teacher = request.user.is_superuser or is_admin(request.user) or is_teacher(request.user)
    if not is_admin_or_teacher:
        return render(request, 'error.html', {'message': 'Access Denied - Only Admin or Teacher can edit students'})
        
    student = None
    for s in Student.objects.all():
        if str(s._id) == str(id):
            student = s
            break
            
    if not student:
        from django.http import Http404
        raise Http404("No Student matches the given query.")

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        
        class_id = request.POST.get("class_id")
        for c in Class.objects.all():
            if str(c._id) == str(class_id):
                student.student_class = c
                break

        student.save()
        return redirect("/students/list/")

    raw_classes = Class.objects.all()
    classes = []
    for c in raw_classes:
        classes.append({
            "mongo_id": str(c.pk),
            "class_name": c.class_name,
            "section": c.section
        })

    student_class_id = str(student.student_class._id) if student.student_class else ""

    return render(request, "students/edit.html", {
        "student": student, 
        "classes": classes,
        "student_class_id": student_class_id
    })


