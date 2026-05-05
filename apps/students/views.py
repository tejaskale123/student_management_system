from django.shortcuts import render, redirect
from .models import Student

# ADD STUDENT
def add_student(request):
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


# LIST STUDENTS
def list_students(request):
    query = request.GET.get("q")

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, "students/list.html", {"students": students})


# DELETE STUDENT
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/students/list/")

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.class_id = request.POST.get("class_id")
        student.save()

        return redirect("/students/list/")

    return render(request, "students/edit.html", {"student": student})