# CS420_Lab03

## Environment Setup (Recommended: GitHub Codespaces)

1. Open this repository in **GitHub Codespaces**
2. Open a terminal and verify Python version (make sure version is 3.8 - 3.13):
   ```bash
   python --version
   ```
3. Change this to the version you have in both setup_example.py and test_parser.py:
```bash
from byte_code.python_311.uabcs_parser import uabcs_parser
from byte_code.python_312.uabcs_parser import uabcs_parser
```
5. cd lab03
   
## Running the Example Script

The provided setup_example.py demonstrates basic usage of the parser.

Run:
```bash
python setup_example.py
```
This will parse student_grades.uabcs and print the resulting records.

### Running Unit Tests

All unit tests are located in test_parser.py.

To run the tests:
```bash
python test_parser.py
```

Expected output: 

<img width="533" height="208" alt="image" src="https://github.com/user-attachments/assets/d20fcb8b-6474-4841-ac35-1625e38b704d" />


