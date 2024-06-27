from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages 
import datetime
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


@login_required
def task_search(request):
    query = request.GET.get('query')
    if query:
        tasks = Task.objects.filter(title__icontains=query, user=request.user)
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/task_search.html', {'tasks': tasks, 'query': query})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully.')  # Add success message
            send_mail(
                'New Task Added',
                f'You have added a new task: {task.title}',
                'from@example.com',
                [request.user.email],
                fail_silently=False,
            )
            return redirect('task_list')  # Redirect to task list or any other page
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})
    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list page after saving
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/delete.html', {'task': task})

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('task_list')

