def _748(lst,words):
    import re
    word=re.findall('[a-z]',lst.lower())
    words.sort(key=lambda x:len(x))
    for i in words:
        flag=1
        li=i.lower()
        for j in set(word):
            if li.count(j)<word.count(j):
                flag=0
                break
        if flag==1:
            return i
    return None
if __name__=='__main__':
    print(_748("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
            
