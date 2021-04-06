'''
第一题题目:给定一个整数数组，找到每个元素的下一个比它的数，存在返回数组内，
其后没有比它大的数则返回None
'''
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
