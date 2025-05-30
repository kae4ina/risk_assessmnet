from django.urls import path
from .views import task_list, update_task_status, create_task_from_measure, create_task_from_user_measure, get_risks, \
    create_measure_and_task

urlpatterns = [
    path('tasks/', task_list, name='task_list'),

path('tasks/update_task_status/<int:task_id>/', update_task_status, name='update_task_status'),
path('tasks/create_from_default_measure/', create_task_from_measure, name='create_from_default_measure'),
path('create-task-from-user-measure/', create_task_from_user_measure, name='create_task_from_user_measure'),
path('get_risks/', get_risks, name='get_risks'),
    path('create-measure-and-task/', create_measure_and_task, name='create_measure_and_task'),
]
