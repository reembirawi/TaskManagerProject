from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all().filter(user_id=3)
    user = User.objects.get(id=3)
    print(user.username)
    context = {
        'user': user,
        'tasks': tasks,
    }
    return render(request=request, template_name='tasks/home.html', context=context)


def create_task(request):
    user = User.objects.get(id=3)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            status = form.cleaned_data["status"]
            Task.objects.create(title=title, description=description, status=status, user=user)
            return HttpResponseRedirect("/")
    else:
        form = TaskForm()
    context = {
        'user': user,
        'form': form,
    }
    return render(request, "tasks/create_task.html", context=context)


def edit_task(request, id):
    user = User.objects.get(id=3)
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TaskForm(instance=task)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, "tasks/edit_task.html", context=context)

def delete_task(request, id):
    user = User.objects.get(id=3)
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect("/")
    context = {
        'user': user,
        'task': task,
    }
    return render(request, "tasks/delete_task.html", context=context)