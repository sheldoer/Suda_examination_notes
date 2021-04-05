import numpy as np
import re
def func1_1():
    #判断两个整数是否互质
    m = eval(input())
    n = eval(input())
    if m <= 1 or n < 1:
        return None
    if m > n:
        m, n = n, m
    return n % m
def func1(m,n):
    #判断两个整数是否互质
    if m<=1 or n<=1:
        return False
    top=int(min(m,n)**0.5)+1    #以最小的数的平方根位上界寻找公因子
    for i in range(2,top):
        if m%i==0 and n%i==0:
            return False
    return True
def func2(lst:list):
    #求一个整数数列的逆序数
    count=0
    for i in range(len(lst)-1):       #计算每个数的逆序数
        for j in range(i+1,len(lst)):  #查看后边是否有小于自己的数
            if lst[i]>lst[j]:
                count+=1
    return count
def matrixmul(A, B):
    if len(A[0]) == len(B):
        res = [[0]*len(B[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    res[i][j] += A[i][k]*B[k][j]
        return res
    return "输出矩阵有误"


def func3():
    mat1 = eval(input("mat1:"))
    mat2 = eval(input("mat2:"))
    result = matrixmul(mat1, mat2)
    print(result)
#def func3(mat1,mat2):
    #矩阵相乘
    #return list(np.array(tuple(mat1))*np.array(tuple(mat2)))


def func4(lst):
    #一维列表转成二维列表
    n=int(len(lst)**0.5)    #根据列表长度判断维度n
    new=[]                  #外层列表
    for i in range(n):
        new1=[]             #要添加的内层列表
        for j in range(n):
            new1.append(lst[i*n+j])
        new.append(new1)
    return new
def func5(s):
    #测试词频，输出词频最高的三个词
    res=s.split()
    keys=list(set(res))                  #建立关键词列表
    values=[res.count(i) for i in keys]   #建立值列表
    dic=sorted(dict(zip(keys,values)).items(),key=lambda x:x[1],reverse=True)#建立词典
    res.clear()
    if len(dic)<3:
        for i in dic:
            res.append(i[0])
    else:
        for i in range(3):
            res.append(dic[i][0])
    return res
def func6(s,t):
    #确定其Jaccard系数的三个统计量a,b,c
    a=b=c=0           #初始化为0，开始计数
    st=set(s+t)
    for i in st:
        if i in s and i in t: #a情况
            a+=1
        elif i in s and i not in t: #b情况
            b+=1
        else:                   #c情况
            c+=1
    return (a,b,c)
def func7(s):
    #统计一个非空字符串中出现次数最多的字符及其出现次数。
    s=s.upper()
    m=0                #标记最大次数
    for i in s:
        if s.count(i)>m:
            m=s.count(i)
            w=i        #标记最大字母
    return [w,m]
def func8(s):
    #
    nums=re.findall('\d{3,5}',s)
    values=[sum(list(map(int,list(i))))/len(i) for i in nums]
    dic=sorted(dict(zip(list(map(int,nums)),values)).items(),key=lambda x:x[1],reverse=True)
    #print(dic)
    keys=[]
    for key,values in dic:
        keys.append(key)
    return keys
if __name__=='__main__':
    #print(bool(func1_1()))
    #print(func1(2,3),func1(4,8))
    #print(func2([4,3,2,1]),func2([1,3,2,4]))
    #print(func3([[1,2]],[[1],[2]]))                 #未作出
    #print(func4([1]),func4([2,1,3,4])
    #print(func5('hello hi hello apple'),func5('a')) #有点小瑕疵
    #print(func6('his','she'),func6('hello','python'))
    #print(func7('1aA'),func7('a'))
    print(func8('123a4567 1'),func8('1234'))
    pass
