def search_distance(s,c):
    allc=[]
    '''
    d=s.index(c)  
    while True:
        allc.append(d)
        d=s.index(c,d)'''
    for i in range(len(s)):
        if s[i]==c:
            allc.append(i)
    print(allc)
    res=[]
    for i in range(len(s)):
        md=min(abs(j-i) for j in allc)
        res.append(md)
    return res
if __name__=='__main__':
     s = 'loveleetcode'
     c = 'e'
     print(search_distance(s,c))
