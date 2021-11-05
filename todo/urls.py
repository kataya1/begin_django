
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.index, name="tasks"),
    path('tasks/<int:task_id>/', views.tasks, name='view_task'),
    path('form', views.form, name='form')
]
