from django.urls import path
from . import views


urlpatterns = [

    path('task_assignment/<int:task_id>/', views.task_assignment, name='task_assignment'),
    path('task_assignment/', views.task_assignment, name='task_assignment'),  # for creating a new task
    path('view_task/', views.view_task, name='view_task'),
    path('reports/', views.reports, name='reports'),
    path('projects/', views.add_project, name='projects'),
    path('feedback/', views.feedback, name='feedback'),
    path('view_project/', views.view_project, name='view_project'),
    path('so2_report/', views.so2_report, name='so2_report'),



]