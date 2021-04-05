import random
import numpy as np
def is_prime(n):
    #判断n是否为素数
    if n<2:
        return False
    if n==2:
        return True
    top=int(n**0.5)+1  #确定判定边界
    for i in range(2,top):
        if n%i==0:
            return False
    return True

def func_13():
    #函数实现，先将500以内的质数存入列表，之后依次输出5个
    res=[]
    for i in range(500):
        if is_prime(i):
            res.append(i)
    j=0
    while j<len(res):
        for i in range(5):
            print(res[j+i],end=' ')
            if j+i+1>=len(res):
                break
        j+=5
        print('\n')

def func_14():
    #对列表进行排序输出
    res=input('please input nums').split()
    res=list(map(int,res))
    print(sorted(set(res)))

def func_15():
    #判断两个字符串是否同构
    s1=sorted(list(input('please input str1:')))
    s2=sorted(list(input('please input str2:')))
    print('yes'if s1==s2 else 'no')

def transpose(M):
    # 直接使用zip解包成转置后的元组迭代器，再强转成list存入最终的list中
    return [list(row) for row in zip(*M)]
def func_16():
    #对数组进行随机赋值，并实现转置
    n=int(input("col:")) #n为矩阵维数
    mar=[]               #mar空矩阵
    for i in range(n):
        col=[]              #一行一行赋值
        for j in range(n):
            col.append(random.randint(1,10)) #对矩阵元素随机赋值
        mar.append(col)
    print(mar)
    print(np.array(mar).T)
    print(transpose(mar))

def func_17():
    #对成绩根据总分从高到低排序，依次输出排序后的列表
    res=[['张飞',78,75],
         ['李大刀',92,67],
         ['李墨白',84,88],
         ['王老虎',50,90],
         ['雷小米',99,98]]
    res.sort(key=lambda x:x[1]+x[2],reverse=True) #根据分数和进行逆排序,从高到低
    for i in range(len(res)):
        print('%8s%8d'%(res[i][0],res[i][1]+res[i][2]))

def func_18():
    #
    n=int(input('num:'))
    row, col = 0, n // 2
    magic = []
    for i in range(n):
        magic.append([0] * n)
    magic[row][col] = 1
    for i in range(2, n * n + 1):
        r, l = (row - 1 + n) % n, (col + 1) % n #########不会
        if (magic[r][l] == 0):
            row, col = r, l
        else:
            row = (row + 1) % n
        magic[row][col] = i
    marray = np.array(magic)
    print(marray)
     

def main():
    #func_13()
    #func_14()
    #func_15()
    func_16()
    #func_17()
    #func_18()
    
    pass
if __name__=='__main__':
    main()
            
