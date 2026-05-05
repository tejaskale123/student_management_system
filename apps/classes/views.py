from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Class

def is_admin(user):
    return user.is_superuser or user.is_staff or user.groups.filter(name__iexact='Admin').exists()

def is_teacher(user):
    return user.groups.filter(name__iexact='Teacher').exists()

# ADD CLASS
@login_required
def add_class(request):
    if not (is_admin(request.user) or is_teacher(request.user)):
        return render(request, 'error.html', {'message': 'Access Denied - Only Admin or Teacher can add classes'})
    
    if request.method == "POST":
        Class.objects.create(
            class_name=request.POST.get("class_name"),
            year=request.POST.get("year"),
            section=request.POST.get("section")
        )
        return redirect("/classes/list/")

    return render(request, "classes/add.html")


# LIST CLASSES
@login_required
def list_classes(request):
    classes = Class.objects.all()
    return render(request, "classes/list.html", {"classes": classes})
