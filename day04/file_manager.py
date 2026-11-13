import csv
import json

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

JSON_FILE = DATA_DIR / "students.json"
CSV_FILE = DATA_DIR / "students.csv"

def ensure_data_directory():
    """Создаёт папку для данных, если она отсутствует."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_to_json(students, file_path=JSON_FILE):
    """Сохраняет список студентов в JSON."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(
            students,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_from_json(file_path=JSON_FILE):
    """Загружает студентов из JSON."""
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"JSON-файл не найден: {file_path}")
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Ошибка: JSON должен содержать список студентов.")
            return []

        return data

    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        print(f"Ошибка чтения JSON: {error}")
        return []


def save_to_csv(students, file_path=CSV_FILE):
    """Сохраняет список студентов в CSV."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["name", "age", "group", "grades"]

    with file_path.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            row = student.copy()
            row["grades"] = json.dumps(row["grades"])
            writer.writerow(row)


def validate_student(student):
    """Проверяет корректность данных одного студента."""
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


def load_from_csv(file_path=CSV_FILE):
    """Загружает студентов из CSV."""
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"CSV-файл не найден: {file_path}")
        return []

    students = []

    try:
        with file_path.open(
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as file:
            reader = csv.DictReader(file)

            required_fields = {"name", "age", "group", "grades"}

            if not required_fields.issubset(reader.fieldnames or []):
                print("Ошибка: в CSV отсутствуют необходимые столбцы.")
                return []

            for row in reader:
                try:
                    if None in row or any(
                        value is None for value in row.values()
                    ):
                        continue

                    student = {
                        "name": row["name"].strip(),
                        "age": int(row["age"]),
                        "group": row["group"].strip(),
                        "grades": json.loads(row["grades"])
                    }

                    student["grades"] = tuple(student["grades"])

                    if validate_student(student):
                        students.append(student)

                except (ValueError, TypeError, json.JSONDecodeError):
                    continue

    except UnicodeDecodeError as error:
        print(f"Ошибка кодировки CSV: {error}")
        return []

    return students

def import_students_from_csv(file_path):
    """Импортирует корректные записи из стороннего CSV."""
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Файл для импорта не найден: {file_path}")
        return [], 0

    imported_students = []
    skipped_rows = 0

    try:
        with file_path.open(
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as file:
            reader = csv.DictReader(file)

            required_fields = {"name", "age", "group", "grades"}

            if not required_fields.issubset(reader.fieldnames or []):
                print("Ошибка: неверная структура CSV.")
                return [], 0

            for row in reader:
                try:
                    if None in row or any(
                        value is None for value in row.values()
                    ):
                        raise ValueError("Неполная строка")

                    student = {
                        "name": row["name"].strip(),
                        "age": int(row["age"]),
                        "group": row["group"].strip(),
                        "grades": tuple(json.loads(row["grades"]))
                    }

                    if not validate_student(student):
                        raise ValueError("Некорректные данные")

                    imported_students.append(student)

                except (ValueError, TypeError, json.JSONDecodeError):
                    skipped_rows += 1

    except UnicodeDecodeError as error:
        print(f"Ошибка кодировки CSV: {error}")
        return [], 0

    return imported_students, skipped_rows