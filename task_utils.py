from datetime import datetime

# Import validation functions
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    valid_title, title_error = validate_task_title(title)
    if not valid_title:
        print(f"Error: {title_error}")
        return

    valid_description, description_error = validate_task_description(description)
    if not valid_description:
        print(f"Error: {description_error}")
        return

    valid_due_date, due_date_error = validate_due_date(due_date)
    if not valid_due_date:
        print(f"Error: {due_date_error}")
        return

    tasks.append({
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    })
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Error: Invalid task index.")
        return

    if tasks[index]["completed"]:
        print("Task is already marked as complete.")
    else:
        tasks[index]["completed"] = True
        print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return pending

    print("Pending Tasks:")
    for i, t in enumerate(pending, 1):
        print(f"{i}. {t['title']} | Due: {t['due_date']} | {t['description']}")
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        print("No tasks added yet.")
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / total) * 100
    print(f"Progress: {completed}/{total} tasks completed ({progress:.2f}%)")
    return progress