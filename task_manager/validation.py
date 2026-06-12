from datetime import datetime


def validate_task_title(title):
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty.")
    if len(title.strip()) < 3:
        raise ValueError("Task title must be at least 3 characters long.")
    return True


def validate_task_description(description):
    if not description or not description.strip():
        raise ValueError("Task description cannot be empty.")
    return True


def validate_due_date(due_date):
    if not due_date or not due_date.strip():
        raise ValueError("Due date cannot be empty.")
    try:
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")

    if parsed_date.date() < datetime.now().date():
        raise ValueError("Due date cannot be in the past.")

    return True