from collections import Counter

def average_grade(student: dict) -> float:
    grades = student["grades"]
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def get_top_students(student_list: list[dict], limit: int = 5) -> list[dict]:
    return sorted(
        student_list,
        key=lambda student: (
            -average_grade(student),
            student["name"].casefold(),
        ),
    )[:limit]

def filter_by_group(student_list: list[dict], group: str) -> list[dict]:
    return [s for s in student_list if s["group"] == group]

def sort_by_age(student_list: list[dict]) -> list[dict]:
    return sorted(student_list, key=lambda s: s["age"])

def sort_by_average_grade(student_list: list[dict]) -> list[dict]:
    return sorted(student_list, key=average_grade, reverse=True)

def find_duplicate_names(student_list: list[dict]) -> dict[str, int]:
    name_counts = Counter(s["name"].casefold() for s in student_list)
    return {name: count for name, count in name_counts.items() if count > 1}

def get_unique_groups(student_list: list[dict]) -> set[str]:
    return {s["group"] for s in student_list}

def get_grade_statistics(student_list: list[dict]) -> dict[str, float]:
    averages = [average_grade(s) for s in student_list]

    if not averages:
        return {"min": 0, "max": 0, "average": 0}

    return {
        "min": min(averages),
        "max": max(averages),
        "average": sum(averages) / len(averages),
    }