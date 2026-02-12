from byte_code.python_311.uabcs_parser import uabcs_parser


def test_column_names_correct():
    
    try:
        parser = uabcs_parser()
        parser.parse_file("student_grades.uabcs")

        expected = ["NAME", "SUBJECT", "GRADE", "PASS", "POINTS"]
        result = parser.get_column_names()

        assert result == expected
        return True
    except Exception:
        return False



def test_column_names_independent():
  

    try:
        parser = uabcs_parser()
        parser.parse_file("student_grades.uabcs")

        cols = parser.get_column_names()
        cols.append("NEW_COLUMN")

        new_cols = parser.get_column_names()

        assert "NEW_COLUMN" not in new_cols
        return True
    except Exception:
        return False


if __name__ == "__main__":
    passed = [
        test_column_names_correct(),
        test_column_names_independent()
    ]

    print("\nTesting get_column_names()")
    print("------------------------------")
    print("Passed " + str(passed.count(True)) + " tests")
    print("Failed " + str(passed.count(False)) + " tests")
    print("")
