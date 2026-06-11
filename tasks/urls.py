from django import template
from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.create_task, name='create_task'),
    path('tasks/<int:id>/edit/', views.edit_task, name='edit_task'),
    path('tasks/<int:id>/delete/', views.delete_task, name='delete_task'),
]