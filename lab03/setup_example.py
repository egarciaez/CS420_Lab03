# Please import the right on based on your python version
# e.g. if you have python 3.10.xx use from byte_code.python_310.uabcs_parser import uabcs_parser
# we have included the byte code for python versions 3.8 - 3.13
from byte_code.python_311.uabcs_parser import uabcs_parser

# Initialize a parser instance
parser = uabcs_parser()

# read a .uabcs file using the parser
data = parser.parse_file('student_grades.uabcs')

# print the data
print(data)