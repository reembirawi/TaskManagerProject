from django.contrib.auth.models import User
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer, UserSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()

        status = self.kwargs.get('status')
        if status:
            return queryset.filter(status=status)
        return queryset


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return User.objects.prefetch_related('tasks').get(pk=pk)
