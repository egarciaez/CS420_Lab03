# Function to test
def add(a, b) -> int:
    return a + b


########## Tester fucntions ##########

def test_correct(a, b):
    try:
        expect = a + b
        assert add(a, b) == expect
        return True
    except Exception as e:
        return False

def test_type():
    try:
        assert isinstance(add(2,2), int)
        return True
    except Exception as e:
        return False


# Execution
if __name__ == "__main__":
    passed = [test_correct(2, 2), test_type()]

    print(f"\nTesting")
    print(f"--------------")
    print(f"Passed " + str(passed.count(True)) + " tests")
    print(f"Failed " + str(passed.count(False)) + " tests")
    print("")