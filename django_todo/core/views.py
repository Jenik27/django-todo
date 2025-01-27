from django.shortcuts import redirect
from django.shortcuts import render

from .forms import TaskForm
from .models import Task


# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, "pages/home.html", {"tasks": tasks, "form": TaskForm()})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")
    return redirect("core:home")


def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect("core:home")
    return redirect("core:home")
