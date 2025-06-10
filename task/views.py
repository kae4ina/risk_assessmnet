import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from measure.models import DefaultMeasure, UserMeasure
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
    measure_type = request.GET.get('measure_type', '')
    task_status = request.GET.get('task_status')


    tasks = Task.objects.filter(
        risk_relations__risk__user=request.user
    ).distinct()


    if selected_company_id and selected_company_id != 'None':
        tasks = tasks.filter(
            risk_relations__risk__company_id=selected_company_id
        )

    if measure_type == 'user':
        tasks = tasks.filter(user_measure__isnull=False)
    elif measure_type == 'default':
        tasks = tasks.filter(default_measure__isnull=False)


    if task_status and task_status != 'None':
        tasks = tasks.filter(status_id=task_status)

    statuses = TaskStatus.objects.all()

    return render(request, 'accounts/all_tasks.html', {
        'tasks': tasks,
        'statuses': statuses,
        'user_companies': user_companies,
        'selected_company_id': selected_company_id,
        'measure_type': measure_type,
        'selected_status': task_status
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
@login_required
@csrf_exempt
def create_task_from_user_measure(request):
    try:

        name = request.POST.get('name')
        description = request.POST.get('description')
        related_company_id = request.POST.get('related_company')
        related_risk_id = request.POST.get('related_risk')


        if not all([name, related_company_id, related_risk_id]):
            return JsonResponse({
                'success': False,
                'error': 'Все обязательные поля должны быть заполнены'
            }, status=400)

        try:
            company = Company.objects.get(id=related_company_id)
            risk = UserRisk.objects.get(
                id=related_risk_id,
                company=company,
                user=request.user  # Проверяем, что риск принадлежит пользователю
            )
        except (Company.DoesNotExist, UserRisk.DoesNotExist) as e:
            return JsonResponse({
                'success': False,
                'error': f'Компания или риск не найдены: {str(e)}'
            }, status=404)


        user_measure = UserMeasure.objects.create(
            name=name,
            description= description,
            related_company=company,
            related_risk=risk
        )


        task = Task.objects.create(
            name=f"{name}",
            description= description,
            user_measure=user_measure,
            status=TaskStatus.objects.get(id=3),
            start_date=timezone.now()
        )


        TaskRisk.objects.create(task=task, risk=risk)

        return JsonResponse({
            'success': True,
            'task_id': task.id,
            'measure_id': user_measure.id,
            'redirect_url': reverse('task_list')
        })

    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Ошибка при создании меры и задачи: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)

@login_required
def get_risks(request):
    company_id = request.GET.get('company_id')
    if not company_id:
        return JsonResponse({'risks': [], 'error': 'Company ID is required'}, status=400)

    try:

        risks = UserRisk.objects.filter(
            company_id=company_id,
            user=request.user
        ).values('id', 'name')

        return JsonResponse({
            'risks': list(risks),
            'success': True
        })
    except Exception as e:
        return JsonResponse({
            'risks': [],
            'error': str(e),
            'success': False
        }, status=500)

import logging
logger = logging.getLogger(__name__)
@csrf_exempt
@require_POST
def create_measure_and_task(request):
    try:
        logger.info("Минимальная рабочая версия")
        return JsonResponse({'success': True, 'test': 'OK'})
    except Exception as e:
        logger.error(f"Ошибка в минимальной версии: {str(e)}")
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
    """   try:
        # Явно получаем только нужные поля
        allowed_fields = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'related_company': request.POST.get('related_company'),
            'related_risk': request.POST.get('related_risk')
        }

        # Проверка заполненности
        if not all(allowed_fields.values()):
            return JsonResponse({
                'success': False,
                'error': 'Все обязательные поля должны быть заполнены'
            }, status=400)

        # Получаем объекты
        company = Company.objects.get(id=allowed_fields['related_company'])
        risk = UserRisk.objects.get(id=allowed_fields['related_risk'])

        # Создаем меру (строго определенные поля)
        user_measure = UserMeasure(
            name=allowed_fields['name'],
            description=allowed_fields['description'],
            related_company=company,
            related_risk=risk
        )
        user_measure.save()  # Явное сохранение без лишних параметров

        # Создаем задачу
        task = Task.objects.create(
            name=f"Задача: {allowed_fields['name']}",
            description=allowed_fields['description'],
            user_measure=user_measure,
            status=TaskStatus.objects.get(id=3)
        )

        # Связь задачи с риском
        TaskRisk.objects.create(task=task, risk=risk)

        return JsonResponse({
            'success': True,
            'task_id': task.id,
            'measure_id': user_measure.id
        })

    except (Company.DoesNotExist, UserRisk.DoesNotExist):
        return JsonResponse({
            'success': False,
            'error': 'Компания или риск не найдены'
        }, status=404)
    except Exception as e:
        import logging
        logging.error(f"Error in create_task_from_user_measure: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Внутренняя ошибка сервера'
        }, status=500)"""