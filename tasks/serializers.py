from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long."
            )

        return value

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "user"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "tasks"]
