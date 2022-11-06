import slate3k as slate
text  = slate.PDF(open('C:/Users/ASUS/Downloads/md (1).pdf', 'rb')).text()
#print(text)
#print(type(text))
import regex as re
name = re.findall("^Name", text)

#print(name)