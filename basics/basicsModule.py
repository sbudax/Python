#Using Builtin Modules

#Usage: import sys
#       sys.builtin_module_names







# import time
# import os

# while True:
#     if os.path.exists("file.txt"):
#         with open("file.txt") as file:
#             print(file.read())
#     else:
#         print("file does not exist")
#     time.sleep(5)             






#Third-Party Modules
# 
# pip/pip3   library in python used to install third-party modules
# 
# usage: pip3 install pandas 

import time             #Builtin library
import os               #Standard library
import pandas           #Third-party library

while True:
    if os.path.exists("temp.csv"):
        data = pandas.read_csv("temp.csv")
        print(data.mean()["st1"])
    else:
        print("file does not exist")
    time.sleep(5)

# In this section you learned that:

# Builtin objects are all objects that are written inside the Python interpreter in C language.

# Builtin modules contain builtins objects.

# Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

# import time
# time.sleep(5)
# A list of all builtin modules can be printed out with:

# import sys
# sys.builtin_module_names
# Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

# Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

# Packages are a collection of .py modules.

# Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

# Third-party libraries can be installed from the terminal/command line:

# Windows:

# pip install pandas

# Mac and Linux:

# pip3 install pandas