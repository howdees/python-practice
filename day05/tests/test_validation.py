import pytest

from student_tools.validation import validate_age, validate_student

@pytest.mark.parametrize("value", ["0", "25", "120", 0, 25, 120])
def test_validate_age_valid(value):
    assert validate_age(value) is True

@pytest.mark.parametrize(
    "value",
    ["-1", "121", "abc", "", None, -1, 121, 3.5, "12.5"],
)
def test_validate_age_invalid(value):
    assert validate_age(value) is False

@pytest.mark.parametrize("value", [True, False])
def test_validate_age_rejects_bool(value):
    assert validate_age(value) is False

def test_validate_student_ok():
    record = {"name": "Анна", "age": 20, "group": "Python-101", "grades": (5, 5, 4)}
    assert validate_student(record) is True

@pytest.mark.parametrize("missing", ["name", "age", "group", "grades"])
def test_validate_student_missing_field(missing):
    record = {"name": "Анна", "age": 20, "group": "Python-101", "grades": (5,)}
    del record[missing]
    assert validate_student(record) is False

@pytest.mark.parametrize("bad_age", ["abc", None, 200, True])
def test_validate_student_bad_age(bad_age):
    record = {"name": "Анна", "age": bad_age, "group": "Python-101", "grades": (5,)}
    assert validate_student(record) is False

@pytest.mark.parametrize("bad_grades", [[], [0], [6], [True], "abc", (5, 5, 4, 5, 6)])
def test_validate_student_bad_grades(bad_grades):
    record = {"name": "Анна", "age": 20, "group": "Python-101", "grades": bad_grades}
    assert validate_student(record) is False