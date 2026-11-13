from pathlib import Path

from day03.students import (
    students,
    average_grade,
    get_grade_statistics,
    get_top_students,
    get_unique_groups,
    find_duplicate_names,
)

from day04.file_manager import (
    save_to_json,
    load_from_json,
    save_to_csv,
    load_from_csv,
    import_students_from_csv,
    JSON_FILE,
    CSV_FILE,
)

REPORTS_DIR = Path(__file__).parent / "reports"
REPORT_FILE = REPORTS_DIR / "report.txt"


def create_report(
    original_students,
    json_students,
    csv_students,
    imported_students,
    skipped_rows
):
    """Формирует текстовый отчёт о работе с файлами."""

    lines = []

    lines.append("ОТЧЁТ ПО РАБОТЕ С ФАЙЛАМИ")
    lines.append("=" * 45)

    lines.append(
        f"Исходное количество студентов: {len(original_students)}"
    )
    lines.append(
        f"Загружено из JSON: {len(json_students)}"
    )
    lines.append(
        f"Загружено из CSV: {len(csv_students)}"
    )

    lines.append("\nСРАВНЕНИЕ ДАННЫХ")
    lines.append("-" * 45)

    if (
        len(original_students) == len(json_students)
        and len(original_students) == len(csv_students)
    ):
        lines.append("Количество записей совпадает.")
    else:
        lines.append("Количество записей не совпадает.")

    lines.append("\nИМПОРТ ИЗ CSV")
    lines.append("-" * 45)
    lines.append(f"Успешно импортировано: {len(imported_students)}")
    lines.append(f"Пропущено некорректных строк: {skipped_rows}")

    statistics = get_grade_statistics(original_students)

    lines.append("\nСТАТИСТИКА УСПЕВАЕМОСТИ")
    lines.append("-" * 45)

    lines.append(
        f"Средний балл: {statistics['average']:.2f}"
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
        get_top_students(original_students),
        start=1
    ):
        lines.append(
            f"{number}. {student['name']} — "
            f"{average_grade(student):.2f}"
        )

    lines.append("\nУНИКАЛЬНЫЕ ГРУППЫ")
    lines.append("-" * 45)

    for group in sorted(get_unique_groups(original_students)):
        lines.append(f"- {group}")

    lines.append("\nПОВТОРЯЮЩИЕСЯ ИМЕНА")
    lines.append("-" * 45)

    duplicates = find_duplicate_names(original_students)

    if duplicates:
        for name, count in sorted(duplicates.items()):
            lines.append(f"{name}: {count}")
    else:
        lines.append("Повторяющихся имён нет.")

    return "\n".join(lines)


def save_report(report):
    """Сохраняет отчёт в текстовый файл."""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with REPORT_FILE.open("w", encoding="utf-8") as file:
        file.write(report)


def main():
    print("СОХРАНЕНИЕ ДАННЫХ")

    # Сохраняем исходные данные
    save_to_json(students)
    save_to_csv(students)

    print(f"JSON сохранён: {JSON_FILE}")
    print(f"CSV сохранён: {CSV_FILE}")

    print("\nЧТЕНИЕ ДАННЫХ")

    # Читаем данные
    json_students = load_from_json()
    csv_students = load_from_csv()

    print(f"Загружено из JSON: {len(json_students)}")
    print(f"Загружено из CSV: {len(csv_students)}")

    print("\nИМПОРТ ИЗ CSV")

    # Импортируем данные из CSV с проверкой строк
    imported_students, skipped_rows = import_students_from_csv(
        CSV_FILE
    )

    print(f"Импортировано: {len(imported_students)}")
    print(f"Пропущено строк: {skipped_rows}")

    print("\nФОРМИРОВАНИЕ ОТЧЁТА")

    report = create_report(
        students,
        json_students,
        csv_students,
        imported_students,
        skipped_rows
    )

    save_report(report)

    print(report)
    print(f"\nОтчёт сохранён: {REPORT_FILE}")


if __name__ == "__main__":
    main()