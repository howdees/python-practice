
from students import (
    students,
    average_grade,
    get_top_students,
    filter_by_group,
    sort_by_age,
    sort_by_average_grade,
    find_duplicate_names,
    get_unique_groups,
    get_grade_statistics,
)


def format_student(student):
    """Формирует строку с информацией об одном студенте."""
    return (
        f'{student["name"]}, '
        f'{student["age"]} лет, '
        f'группа: {student["group"]}, '
        f'средний балл: {average_grade(student):.2f}'
    )


def create_report(student_list):
    """Формирует полный текстовый отчёт по студентам."""
    lines = []

    lines.append("ОТЧЁТ ОБ УСПЕВАЕМОСТИ СТУДЕНТОВ")
    lines.append("=" * 45)

    lines.append(f"Всего студентов: {len(student_list)}")

    statistics = get_grade_statistics(student_list)

    lines.append(
        f"Средний балл группы: {statistics['average']:.2f}"
    )
    lines.append(
        f"Минимальный средний балл: {statistics['min']:.2f}"
    )
    lines.append(
        f"Максимальный средний балл: {statistics['max']:.2f}"
    )

    lines.append("\nТОП-5 СТУДЕНТОВ")
    lines.append("-" * 45)

    for number, student in enumerate(
        get_top_students(student_list),
        start=1
    ):
        lines.append(
            f"{number}. {format_student(student)}"
        )

    lines.append("\nСТУДЕНТЫ ПО ГРУППАМ")
    lines.append("-" * 45)

    for group in sorted(get_unique_groups(student_list)):
        group_students = filter_by_group(student_list, group)

        lines.append(f"\n{group} — {len(group_students)} студентов")

        for student in group_students:
            lines.append(f"  {format_student(student)}")

    lines.append("\nСОРТИРОВКА ПО ВОЗРАСТУ")
    lines.append("-" * 45)

    for student in sort_by_age(student_list):
        lines.append(f"- {format_student(student)}")

    lines.append("\nСОРТИРОВКА ПО СРЕДНЕМУ БАЛЛУ")
    lines.append("-" * 45)

    for student in sort_by_average_grade(student_list):
        lines.append(f"- {format_student(student)}")

    lines.append("\nПОВТОРЯЮЩИЕСЯ ИМЕНА")
    lines.append("-" * 45)

    duplicates = find_duplicate_names(student_list)

    if duplicates:
        for name, count in sorted(duplicates.items()):
            lines.append(f"{name}: {count} раза")
    else:
        lines.append("Повторяющихся имён нет.")

    lines.append("\nУНИКАЛЬНЫЕ ГРУППЫ")
    lines.append("-" * 45)

    for group in sorted(get_unique_groups(student_list)):
        lines.append(f"- {group}")

    return "\n".join(lines)


def save_report(report, filename="day03/report.txt"):
    """Сохраняет отчёт в текстовый файл."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)


def main():
    report = create_report(students)

    print(report)

    save_report(report)

    print("\nОтчёт сохранён в файл day03/report.txt")


if __name__ == "__main__":
    main()
