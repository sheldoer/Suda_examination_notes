def _561(lst):
    lst.sort()
    res=[]
    for i in range(len(lst)//2):
        tem=[lst[2*i],lst[2*i+1]]
        res.append(tem)
    num=0
    for i in res:
        num+=min(i)
    return num
if __name__=='__main__':
    print(_561( [1,4,3,2]))
