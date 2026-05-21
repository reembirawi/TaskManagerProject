# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from django.contrib.auth.models import User
from django.db.models import Count
from tasks.models import Task

def run():
    # Write any test code you want here
    users = User.objects.annotate(total=Count('task'))
    for u in users:
        print(f"User: {u.username}, Tasks: {u.total}")

if __name__ == "__main__":
    run()