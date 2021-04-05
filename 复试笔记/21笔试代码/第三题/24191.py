def find_pair(L):
    length=len(L)
    mxmul=L[0]*L[1]
    indext=(L[0],L[1])
    for i in range(length):
        for j in range(i+1,length):
            if L[i]*L[j]>=mxmul:
                mxmul=L[i]*L[j]
                indext=(L[i],L[j])
    indext=list(indext)
    indext.sort()
    return (indext[0],indext[1])
            



if __name__=='__main__':
    #L=[1,-1,0]
    L=[-10,-3,5,6,-2]
    print(find_pair(L))
