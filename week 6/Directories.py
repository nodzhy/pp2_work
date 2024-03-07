import os
from string import ascii_uppercase
# task 1
'''
location1 = r'C:\\'
print([name for name in os.listdir(location1)]) 
print([name for name in os.listdir(location1) if os.path.isdir(os.path.join(location1, name))])
print([name for name in os.listdir(location1) if not os.path.isdir(os.path.join(location1, name))]) 
'''
#task 2
"""
print('Path exists:', os.access('builtin.py', os.F_OK))
print('Path readable:', os.access('builtin.py', os.R_OK))
print('Path writable:', os.access('builtin.py', os.W_OK))
print('Path executable:', os.access('builtin.py', os.X_OK))
"""
#task 3
"""
with open ('builtin.py', 'r') as path:
   path_check=os.access(path, os.F_OK)
if path_check==True:
     print("Directories:", ', '.join([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]))
     print("Files:", ', '.join([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]))
else:
     print("such file not found")
"""
#task 4
'''
with open("builtin.py", "r") as file:
    x = len(file.readlines())
    print("Number of lines:", x)
'''
#task 5
"""48-
my_list=["apple", "banana", "orange", "milk"]
with open ("1.txt,", "w") as file:
    file.write(str(my_list))
    print("")
"""
#task 6
"""
import string

for letter in string.ascii_lowercase:
    name=f"letter_{letter}.txt"
    with open(name, "w") as file:
        file.write(f"this is file {letter} from Directories.py\n")
"""
#task 7
"""
with open ('yourfile1.txt', 'r') as file_first, open('yourfile2.txt', 'a') as file_second:
    for i in file_first:
        file_second.write(i)
"""
#task 8
"""
path=r'C:\yourfile.txt'
path_check=os.access(path, os.F_OK)
if path_check==True:
    os.remove(path)
    print("file was deleted")
else:
    print("such file not found")
"""