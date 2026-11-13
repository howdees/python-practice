import pytest

from student_tools.analysis import (
    average_grade,
    filter_by_group,
    find_duplicate_names,
    get_grade_statistics,
    get_top_students,
    get_unique_groups,
    sort_by_age,
    sort_by_average_grade,
)
from student_tools.data import students

def test_average_grade_normal():
    assert average_grade({"grades": (5, 5, 4, 5)}) == pytest.approx(4.75)

def test_average_grade_empty_returns_float():
    result = average_grade({"grades": ()})
    assert isinstance(result, float)
    assert result == 0.0

def test_get_top_students_default():
    top = get_top_students(students)
    assert len(top) == 5
    assert top[0]["name"] == "Мария"
    assert average_grade(top[0]) == pytest.approx(5.0)

def test_get_top_students_custom_limit():
    assert len(get_top_students(students, limit=3)) == 3

def test_filter_by_group():
    result = filter_by_group(students, "Python-101")
    assert len(result) == 5
    assert all(s["group"] == "Python-101" for s in result)

def test_filter_by_group_unknown():
    assert filter_by_group(students, "Python-999") == []

def test_sort_by_age():
    result = sort_by_age(students)
    ages = [s["age"] for s in result]
    assert ages == sorted(ages)

def test_sort_by_average_grade():
    result = sort_by_average_grade(students)
    averages = [average_grade(s) for s in result]
    assert averages == sorted(averages, reverse=True)

def test_find_duplicate_names():
    duplicates = find_duplicate_names(students)
    assert duplicates.get("иван") == 2
    assert duplicates.get("мария") == 2

def test_find_duplicate_names_none():
    data = [{"name": "Анна", "grades": (5,)}, {"name": "Борис", "grades": (4,)}]
    assert find_duplicate_names(data) == {}

def test_get_unique_groups():
    groups = get_unique_groups(students)
    assert groups == {"Python-101", "Python-102", "Python-103"}

def test_get_grade_statistics():
    stats = get_grade_statistics(students)
    assert stats["min"] == pytest.approx(3.5)
    assert stats["max"] == pytest.approx(5.0)
    assert stats["average"] == pytest.approx(4.3166, abs=1e-3)