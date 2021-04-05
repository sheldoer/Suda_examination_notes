file=open('1.txt','r',encoding='gb18030')
juzi=file.readlines()
print(x for x in juzi)
file.close()
