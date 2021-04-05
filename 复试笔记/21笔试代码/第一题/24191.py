def find_next(L):
    length=len(L)
    res=[]
    for i in range(length):
        flag=0                     #flag
        for j in range(i+1,length):
            if L[j]>L[i]:
                res.append(L[j])
                flag=1
                break
        if flag==0:
            res.append(None)
    return res
if __name__=='__main__':
    L=[2,3,5]
    L=[5,2,3]
    print(find_next(L))
