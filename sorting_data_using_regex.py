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
bill_number = re.search(r'Bill No :(.*?)Ref',text).group(1)
doctor = re.search(r'ortho Done by :(.*?)Bill',text).group(1)
date = re.search(r'Date :(.*?)Remarks',text).group(1)
remarks = re.search(r'Remarks :(.*?)Auth',text).group(1)
service = re.search(r'Amount 1(.*?)[1-9.*]',text).group(1)
amount = re.search(r'Total :(.*)',text).group(1)

