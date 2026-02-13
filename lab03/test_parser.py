
from byte_code.python_312.uabcs_parser import uabcs_parser


########## Tester functions ##########

def testValidFile():
    """
    Tests that it is a valid .uabcs file 
    for parse_file(self, filename) function

    """
    try:
        parser = uabcs_parser()
        records = parser.parse_file("student_grades.uabcs")

        assert isinstance(records, list)
        assert len(records) == 10

        assert records[0]["NAME"] == "Alice"
        assert isinstance(records[0]["GRADE"], int)
        assert records[0]["GRADE"] == 85
        assert records[0]["PASS"] is True

        return True
    except Exception as e:
        print("Error in test_parse_file_valid:", e)
        return False


def testInvalidFileExtension():
    """
    Tests that an invalid file extension raises ValueError 
    for parse_file(self, filename) function
    """
    try:
        parser = uabcs_parser()
        parser.parse_file("student_grades.cs")

        # If no error is raised, test should fail
        return False

    except ValueError:
        return True

    except Exception as e:
        print("Unexpected error type:", e)
        return False


"""
get_column_names function tests
"""
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

"""
get_records_by_field() function tests
"""


########## Execution ##########

if __name__ == "__main__":
    passed = [testValidFile(), testInvalidFileExtension()]

    print("\nTesting parse_file():")
    print("----------------------")
    print("Passed:", passed.count(True))
    print("Failed:", passed.count(False))
    print("")


    passed = [
        test_column_names_correct(),
        test_column_names_independent()
    ]

    print("\nTesting get_column_names()")
    print("------------------------------")
    print("Passed " + str(passed.count(True)) + " tests")
    print("Failed " + str(passed.count(False)) + " tests")
    print("")


