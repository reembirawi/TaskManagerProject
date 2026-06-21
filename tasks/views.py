from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/home.html"
    context_object_name = 'tasks'

    def get_queryset(self):
        status = self.kwargs.get("status")
        if status:
            return Task.objects.filter(
                user=self.request.user,
                status=status
            )
        else:
            return Task.objects.filter(
                user=self.request.user
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_status"] = self.kwargs.get("status")
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "status"]
    success_url = '/tasks/'
    template_name = "tasks/create_task.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/tasks/'
    template_name = "tasks/delete_task.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = '/tasks/'
    fields = ["title", "description", "status"]
    template_name = "tasks/edit_task.html"
