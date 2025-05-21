import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_POST

from measure.models import DefaultMeasure
from .models import Task, TaskStatus, TaskRisk
from django.http import JsonResponse
from solver.models import UserRisk
from company.models import Company
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from company.models import CompanyUser


@login_required
def task_list(request):

    user_company_relations = CompanyUser.objects.filter(user=request.user).select_related('company')
    user_companies = [rel.company for rel in user_company_relations]


    selected_company_id = request.GET.get('company_id')


    tasks = Task.objects.filter(
        risk_relations__risk__user=request.user
    ).distinct()


    if selected_company_id:
        tasks = tasks.filter(
            risk_relations__risk__company_id=selected_company_id
        )

    statuses = TaskStatus.objects.all()

    return render(request, 'accounts/all_tasks.html', {
        'tasks': tasks,
        'statuses': statuses,
        'user_companies': user_companies,
        'selected_company_id': int(selected_company_id) if selected_company_id else None
    })

@csrf_exempt
@require_POST
def update_task_status(request, task_id):
    try:
        try:
            data = json.loads(request.body)
            status_id = data.get('status_id')
            if not status_id:
                return JsonResponse({'success': False, 'error': 'Status ID is required'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

        try:
            task = Task.objects.get(id=task_id)
            new_status = TaskStatus.objects.get(id=status_id)
            old_status = task.status
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)
        except TaskStatus.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Status not found'}, status=404)

        # Проверяем, меняется ли статус на "Выполнено"
        if (new_status.name.lower() == "выполнено" and
                (old_status.name.lower() != "выполнено" or not task.end_date)):
            task.end_date = timezone.now()

        task.status = new_status
        task.save()

        return JsonResponse({
            'success': True,
            'new_status_name': new_status.name,
            'end_date': task.end_date.isoformat() if task.end_date else None
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
        risk_id = data.get('risk_id')

        if not measure_id or not risk_id:
            return JsonResponse({'success': False, 'error': 'measure_id and risk_id are required'}, status=400)

        try:
            measure = DefaultMeasure.objects.get(id=measure_id)
            risk = UserRisk.objects.get(id=risk_id)


            task = Task.objects.create(
                name=measure.name,
                default_measure=measure,
                status=TaskStatus.objects.get(id=3)
            )


            TaskRisk.objects.create(
                task=task,
                risk=risk
            )

            return JsonResponse({
                'success': True,
                'task_id': task.id,
                'measure_id': measure.id
            })

        except DefaultMeasure.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Measure not found'}, status=404)
        except UserRisk.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Risk not found'}, status=404)

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)