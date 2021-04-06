'''
第三题题目:给定指定整数数组，找到数组中乘积最大的两个数字，
并以元组的形式返回这两个数字,并且这两个数字从小到大排序

'''
def find_pair(L):
    length=len(L)
    mxmul=L[0]*L[1]
    indext=(L[0],L[1])
    for i in range(length):
        for j in range(i+1,length):
            if L[i]*L[j]>=mxmul:
                mxmul=L[i]*L[j]
                indext=[L[i],L[j]]
    return tuple(sorted(indext))
            
if __name__=='__main__':
    #L=[1,-1,0]
    L=[-10,-3,5,6,-2]
    print(find_pair(L))
