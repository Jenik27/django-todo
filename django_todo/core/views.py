from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import TaskForm
from .models import Task


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "pages/home.html", {"tasks": tasks, "form": TaskForm()})


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("core:home")
    return redirect("core:home")


@login_required
def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        if task.user == request.user:  # Security check
            task.delete()
        return redirect("core:home")
    return redirect("core:home")
