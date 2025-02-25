from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Получаем все задачи
    return render(request, 'accounts/all_tasks.html', {'tasks': tasks})
