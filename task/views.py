import json


from django.shortcuts import render
from .models import Task, TaskStatus
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

def task_list(request):
    tasks = Task.objects.all()
    statuses = TaskStatus.objects.all()
    return render(request, 'accounts/all_tasks.html', {
        'tasks': tasks,
        'statuses': statuses
    })


@csrf_exempt
def update_task_status(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)
            new_status_id = data.get('status_id')

            if new_status_id:
                new_status = TaskStatus.objects.get(id=new_status_id)
                task.status = new_status
                task.save()
                return JsonResponse({'success': True})

            return JsonResponse({'success': False, 'error': 'No status_id provided'})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
        except TaskStatus.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Status not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
