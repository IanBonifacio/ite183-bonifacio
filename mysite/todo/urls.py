from django.urls import path
from .views import TaskListAPI, TaskDetailAPI
from .views import task_list, task_create, task_edit, task_delete

urlpatterns = [
    path('api/tasks/', TaskListAPI.as_view(), name='task_list_api'),
    path('api/tasks/<int:pk>/', TaskDetailAPI.as_view(), name='task_detail_api'),
    path('', task_list, name='task_list'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]