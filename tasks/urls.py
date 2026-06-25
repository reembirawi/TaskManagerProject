from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('tasks/<int:pk>/', views.TaskDetail.as_view(),
         name='task-detail'),
    path('tasks/', views.TaskList.as_view(),
         name='task-list'),
    path('tasks/<str:status>/', views.TaskList.as_view(),
         name='task-list-by-status'),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
