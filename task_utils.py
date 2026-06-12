from datetime import datetime
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)

        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")

    except ValueError as e:
        print(e)

def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        raise ValueError("Invalid task index.")

    tasks[index]["completed"] = True
    print("Task marked as complete!")
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending_tasks):
            print(
                f"{i}: {task['title']} | "
                f"{task['description']} | "
                f"{task['due_date']}"
            )

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100
    return progress