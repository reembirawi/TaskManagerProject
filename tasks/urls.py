from django import template
from django.urls import path
from django.views import View

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='tasks_all'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='create_task'),

    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='edit_task'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),

    path('tasks/<str:status>/', views.TaskListView.as_view(), name='tasks_by_status'),
]