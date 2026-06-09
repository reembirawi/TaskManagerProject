from django.db.models import Count
from tasks.models import TaskStatus
from tasks.models import Task
from django.db import connection, reset_queries

def filter_tasks_by_status(status='done'):
    done_tasks = Task.objects.filter(status=status)

    for task in done_tasks:
        print(f'Task {task.id} is {status}')

def count_tasks_per_status():
    tasks = Task.objects.values('status').annotate(total=Count('id'))

    for task in tasks:
        print(f"{task['status']}: {task['total']}")

def select_task_with_owner():
    tasks = Task.objects.select_related('user')
    for task in tasks:
        print(f'The owner of {task.title} task is {task.user}')

def run():
    print('filter task by status:')
    filter_tasks_by_status(TaskStatus.OPEN.value)
    print()

    print('count tasks per status using annotate():')
    count_tasks_per_status()
    print()

    print('get all tasks with owner data in one query using select_related():')
    select_task_with_owner()
    print()

    print('Verify query counts with django.db.connection.queries:')
    print(f"Total SQL queries executed: {len(connection.queries)}")

    for query in connection.queries:
        print(f"SQL query: {query['sql']}")
        print(f"Time taken: {query['time']} seconds\n")
