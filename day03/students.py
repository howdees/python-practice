from collections import Counter

# Первым делом создаем список студентов. У каждого студента есть имя, возраст, группа и кортеж оценок.
students = [
    {"name": "Анна", "age": 20, "group": "Python-101", "grades": (5, 5, 4, 5)},
    {"name": "Иван", "age": 22, "group": "Python-102", "grades": (4, 3, 5, 4)},
    {"name": "Мария", "age": 19, "group": "Python-101", "grades": (5, 5, 5, 5)},
    {"name": "Алексей", "age": 21, "group": "Python-103", "grades": (3, 4, 4, 5)},
    {"name": "Ольга", "age": 23, "group": "Python-102", "grades": (4, 5, 4, 4)},
    {"name": "Дмитрий", "age": 20, "group": "Python-103", "grades": (5, 4, 5, 5)},
    {"name": "Елена", "age": 18, "group": "Python-101", "grades": (4, 4, 5, 5)},
    {"name": "Иван", "age": 24, "group": "Python-102", "grades": (3, 4, 3, 4)},
    {"name": "Сергей", "age": 22, "group": "Python-103", "grades": (5, 5, 4, 5)},
    {"name": "Наталья", "age": 21, "group": "Python-101", "grades": (4, 5, 5, 4)},
    {"name": "Павел", "age": 19, "group": "Python-102", "grades": (3, 4, 4, 3)},
    {"name": "Мария", "age": 20, "group": "Python-103", "grades": (5, 4, 5, 5)},
    {"name": "Кирилл", "age": 23, "group": "Python-101", "grades": (4, 4, 4, 5)},
    {"name": "Татьяна", "age": 18, "group": "Python-102", "grades": (5, 5, 4, 5)},
    {"name": "Роман", "age": 25, "group": "Python-103", "grades": (3, 3, 4, 4)},
]


def average_grade(student):
    """Вычисляет средний балл одного студента."""
    grades = student["grades"]

    if not grades:
        return 0

    return sum(grades) / len(grades)


def get_top_students(student_list, limit=5):
    """Возвращает студентов с самыми высокими средними баллами."""
    return sorted(
        student_list,
        key=lambda student: (
            -average_grade(student),
            student["name"].casefold()
        )
    )[:limit]


def filter_by_group(student_list, group):
    """Возвращает студентов указанной группы."""
    return [
        student
        for student in student_list
        if student["group"] == group
    ]


def sort_by_age(student_list):
    """Сортирует студентов по возрасту от младшего к старшему."""
    return sorted(
        student_list,
        key=lambda student: student["age"]
    )


def sort_by_average_grade(student_list):
    """Сортирует студентов по среднему баллу по убыванию."""
    return sorted(
        student_list,
        key=average_grade,
        reverse=True
    )


def find_duplicate_names(student_list):
    """Возвращает имена, которые встречаются больше одного раза."""
    name_counts = Counter(
        student["name"].casefold()
        for student in student_list
    )

    return {
        name: count
        for name, count in name_counts.items()
        if count > 1
    }


def get_unique_groups(student_list):
    """Возвращает множество уникальных учебных групп."""
    return {
        student["group"]
        for student in student_list
    }


def get_grade_statistics(student_list):
    """Возвращает минимальный, максимальный и средний баллы."""
    averages = [
        average_grade(student)
        for student in student_list
    ]

    if not averages:
        return {
            "min": 0,
            "max": 0,
            "average": 0
        }

    return {
        "min": min(averages),
        "max": max(averages),
        "average": sum(averages) / len(averages)
    }
