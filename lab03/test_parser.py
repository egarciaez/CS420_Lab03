
from byte_code.python_312.uabcs_parser import uabcs_parser


########## Tester functions ##########

def testValidFile():
    """
    Tests that a valid .uabcs file
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
    Tests that an invalid file extension raises ValueError.
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


########## Execution ##########

if __name__ == "__main__":
    passed = [
        testValidFile(), testInvalidFileExtension()
    ]

    print("\nTesting parse_file():")
    print("----------------------")
    print("Passed:", passed.count(True))
    print("Failed:", passed.count(False))
    print("")




