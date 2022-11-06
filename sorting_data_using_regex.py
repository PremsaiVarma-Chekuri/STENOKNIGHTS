"""import sys
sys.path.insert(1, 'C:/Users/ASUS/Desktop/STENOKNIGHTS/extract_data.py')"""
from extract_data import *
"""name = text.split('Name').pop(1).split('Age').pop(0).strip(" ").strip(":")
print(name)
age = text.split('Age/Sex').pop(1).split('Bill No').pop(0).strip(" ").strip(":")
print(age)"""
x = text

import regex as re
name = re.search(r'Name :(.*?)Age',text).group(1)
age = re.search(r'Age/Sex :(.*?)Bill',text).group(1)
print(age)
