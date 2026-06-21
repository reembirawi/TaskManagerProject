from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task


@method_decorator(login_required, name="dispatch")
class TaskListView(ListView):
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


@method_decorator(login_required, name="dispatch")
class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description", "status"]
    success_url = '/tasks/'
    template_name = "tasks/create_task.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # ← assign the user before saving
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/tasks/'
    template_name = "tasks/delete_task.html"


@method_decorator(login_required, name="dispatch")
class TaskUpdateView(UpdateView):
    model = Task
    success_url = '/tasks/'
    fields = ["title", "description", "status"]
    template_name = "tasks/edit_task.html"
