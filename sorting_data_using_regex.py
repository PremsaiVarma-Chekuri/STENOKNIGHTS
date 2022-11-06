"""import sys
sys.path.insert(1, 'C:/Users/ASUS/Desktop/STENOKNIGHTS/extract_data.py')"""
#from extract_data import *
"""name = text.split('Name').pop(1).split('Age').pop(0).strip(" ").strip(":")
print(name)
age = text.split('Age/Sex').pop(1).split('Bill No').pop(0).strip(" ").strip(":")
print(age)"""
import slate3k as slate
text  = slate.PDF(open('C:/Users/ASUS/Downloads/md (1).pdf', 'rb')).text()
x = text
#print(text)
# text = "xyz hospital Pat.No : 676637 Dept. : Pat.Cat : Pat.Name : sanjeev Age/Sex :18/Male Bill No :45 Ref.By : ortho Done by : robin Bill Date : 5/11/2022 Remarks : --- Auth.By: MS S.No invest igat ion / Service Name Amount 1 ortho therapy session 1,500 Signature Total : 1,500"
import regex as re
name = re.search(r'Name :(.*?)Age',text).group(1)
age = re.search(r'Age/Sex :(.*?)Bill',text).group(1)
bill_number = re.search(r'Bill No :(.*?)Ref',text).group(1)
doctor = re.search(r'ortho Done by :(.*?)Bill',text).group(1)
date = re.search(r'Date :(.*?)Remarks',text).group(1)
remarks = re.search(r'Remarks :(.*?)Auth',text).group(1)
service = re.search(r'Amount 1(.*?)[1-9.*]',text).group(1)
amount = re.search(r'Total :(.*)',text).group(1)
print(age)

