# test_parser.py
import pytest

# Same import as setup_example.py
from byte_code.python_312.uabcs_parser import uabcs_parser


def test_parse_file_valid_student_grades():
    parser = uabcs_parser()
    records = parser.parse_file("student_grades.uabcs")

    assert isinstance(records, list)
    assert len(records) == 10

    assert records[0]["NAME"] == "Alice"
    assert records[0]["GRADE"] == 85
    assert records[0]["PASS"] is True

def test_parse_file_invalid_extension():
    parser = uabcs_parser()

    with pytest.raises(ValueError):
        parser.parse_file("student_grades.cs")

