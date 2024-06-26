from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), # default view - shows all tasks
    path('tasks/search/', views.task_search, name='task_search'),
    path('add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
