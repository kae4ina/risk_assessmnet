import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST

from measure.models import DefaultMeasure
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
@require_POST
def update_task_status(request, task_id):
    try:
        # Проверка и парсинг JSON
        try:
            data = json.loads(request.body)
            status_id = data.get('status_id')
            if not status_id:
                return JsonResponse({'success': False, 'error': 'Status ID is required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

        # Получение объектов
        try:
            task = Task.objects.get(id=task_id)
            status = TaskStatus.objects.get(id=status_id)
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)
        except TaskStatus.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Status not found'}, status=404)

        # Обновление статуса
        task.status = status
        task.save()

        return JsonResponse({
            'success': True,
            'new_status_name': status.name
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Task, DefaultMeasure


@csrf_exempt
@require_POST
def create_task_from_measure(request):
    try:
        data = json.loads(request.body)
        measure_id = data.get('measure_id')

        if not measure_id:
            return JsonResponse({'success': False, 'error': 'measure_id is required'}, status=400)


        try:
            measure = DefaultMeasure.objects.get(id=measure_id)
        except DefaultMeasure.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Measure not found'}, status=404)

        task = Task.objects.create(
            name=measure.name,
            default_measure=measure,
           # related_company=request.user.company,
            status=TaskStatus.objects.first()
        )

        return JsonResponse({
            'success': True,
            'task_id': task.id,
            'measure_id': measure.id
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)