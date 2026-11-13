from typing import Any

def validate_age(value: Any) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, float):
        return False
    try:
        age = int(value)
    except (ValueError, TypeError):
        return False
    return 0 <= age <= 120

def validate_student(student: Any) -> bool:

    if not isinstance(student, dict):
        return False

    required_fields = {"name", "age", "group", "grades"}
    if not required_fields.issubset(student):
        return False

    name = student["name"]
    group = student["group"]
    age = student["age"]
    grades = student["grades"]

    if not isinstance(name, str) or not name.strip():
        return False

    if not isinstance(group, str) or not group.strip():
        return False

    if isinstance(age, bool) or not isinstance(age, int):
        return False

    if not 0 <= age <= 120:
        return False

    if not isinstance(grades, (list, tuple)) or not grades:
        return False

    if any(
        isinstance(grade, bool)
        or not isinstance(grade, (int, float))
        or not 1 <= grade <= 5
        for grade in grades
    ):
        return False

    return True