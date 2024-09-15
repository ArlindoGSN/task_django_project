from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('tasks/<uuid:id>/', views.TaskDetail.as_view(), name='task-detail'),  # Para detalhes, atualização ou exclusão de tarefa específica
]
