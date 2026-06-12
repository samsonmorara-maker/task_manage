from datetime import datetime
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

tasks = []


def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Error: {e}")
        return

    tasks.append({
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    })
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Error: Invalid task index.")
        return

    if tasks[index]["completed"]:
        print("Task is already marked as complete.")
    else:
        tasks[index]["completed"] = True
        print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return pending

    print("Pending Tasks:")
    for i, t in enumerate(pending, 1):
        print(f"{i}. {t['title']} | Due: {t['due_date']} | {t['description']}")
    return pending


def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        print("No tasks added yet.")
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / total) * 100
    print(f"Progress: {completed}/{total} tasks completed ({progress:.2f}%)")
    return progress