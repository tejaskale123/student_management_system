from django.shortcuts import render, redirect
from .models import Class

# ADD CLASS
def add_class(request):
    if request.method == "POST":
        Class.objects.create(
            class_name=request.POST.get("class_name"),
            year=request.POST.get("year"),
            section=request.POST.get("section")
        )
        return redirect("/classes/list/")

    return render(request, "classes/add.html")


# LIST CLASSES
def list_classes(request):
    classes = Class.objects.all()
    return render(request, "classes/list.html", {"classes": classes})