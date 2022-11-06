import slate3k as slate
text  = slate.PDF(open('C:/Users/ASUS/Downloads/md (1).pdf', 'rb')).text()
print(text)