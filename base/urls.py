
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('list/<str:pk>/', views.tasklist, name='list'),
    path('addlist/', views.addTaskList, name='addlist'),
    path('deletelist/<str:pk>/', views.deleteTaskList, name='delete-list'),
    path('updatlist/<str:pk>/', views.updateList, name='update-list'),

    path('deletetask/<str:pk>/', views.deleteTask, name='delete-task'),
    path('completetask/<str:pk>', views.completeTask, name='achieve-task'),
]