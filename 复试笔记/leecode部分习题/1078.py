import re
def find_third(s,first,second):
    #查找指定字符后的单词
    dest=re.findall(f'{first}\s{second}\s\w+',s)
    print(dest)
    res=[]
    for i in dest:
        res.append(i.split()[-1])
    print(res)
s = "we will we will rock you"
first = "we"
second = "will"
find_third(s,first,second)
