from .analysis import (
    average_grade,
    filter_by_group,
    find_duplicate_names,
    get_grade_statistics,
    get_top_students,
    get_unique_groups,
    sort_by_age,
    sort_by_average_grade,
)
from .validation import validate_age, validate_student

__all__ = [
    "average_grade",
    "filter_by_group",
    "find_duplicate_names",
    "get_grade_statistics",
    "get_top_students",
    "get_unique_groups",
    "sort_by_age",
    "sort_by_average_grade",
    "validate_age",
    "validate_student",
]

__version__ = "0.1.0"