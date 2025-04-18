from django.urls import path
from .views import task_list, update_task_status

urlpatterns = [
    path('tasks/', task_list, name='task_list'),

path('tasks/update_task_status/<int:task_id>/', update_task_status, name='update_task_status'),
]
