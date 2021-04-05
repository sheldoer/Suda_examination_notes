def find_major(L):
    length=len(L)
    lst=[]
    res=set()
    for i in L:
        for j in list(i):
            lst.append(j)
    for i in set(lst):
        if lst.count(i)>length/2:
            res.add(i)
    if len(res)>0:
        return res


if __name__=='__main__':
    L=[{1},{1,2},{1}]
    L=[{1},{2,3}]
    print(find_major(L))
    
