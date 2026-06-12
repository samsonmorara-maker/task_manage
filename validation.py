from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")

def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")