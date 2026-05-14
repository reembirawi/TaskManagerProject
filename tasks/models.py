from django.db import models
from django.contrib.auth.models import User
from .decorators import log_call


class TaskStatus(models.TextChoices):
    OPEN = "not-started", "Not Started"
    IN_PROGRESS = "in-progress", "In Progress"
    DONE = "done", "Done"

class TaskManager(models.Manager):

    def open(self):
        return self.filter(status=TaskStatus.OPEN.value)

    def in_progress(self):
        return self.filter(status=TaskStatus.IN_PROGRESS)

    def done(self):
        return self.filter(status=TaskStatus.DONE)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.OPEN.value,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    @log_call
    def assign(self, user: User):
        self.user = user
        self.status = TaskStatus.IN_PROGRESS
        self.save()

    @log_call
    def complete(self):
        self.status = TaskStatus.DONE
        self.save()

    objects = TaskManager()

    class Meta:
        ordering = ["-id"]
    def __str__(self):
        return self.title