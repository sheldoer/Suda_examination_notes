def func_26():
    #输出指定数目用*构成的等腰三角形
    n=int(input('please input a number:'))
    for i in range(n):
        print('{1:^{0}}'.format(n*2-1,((2*i)+1)*'*')) #根据位置依次输出指定数目的*,并居中输出
def func_27():
    #输出乘法口诀表
    n=int(input('please input a number:')) #确定维度
    for i in range(1,n+1):
        for j in range(1,1+i):
            print(i*j,end='\t')
        print('\n')
                  
def func_28():
    #输出指定边长的以*号构成的正六边形
    n=int(input('please input a number:'))   #未作出
    for i in range(1,n*2):
        for j in range(i):
            print('*',end='\t')
        print('\n')
def func_29():
    #求几个数的和
    n=int(input('Please input the number of numbers：')) #确定维度
    while n!=0:   #当n不为0时继续
        nums=0     #和重置为0
        for i in range(n):
            nums+=int(input('Please input number%d:'%(i+1))) #依次输入每一个数
        print('sum=',nums)
        n=int(input('Please input the number of numbers：')) #继续输入数字个数
def is_prime(n):
    #判断n是否为素数
    if n<2:         #小于2无质数
        return False
    if n==2:         #等于2就是质数
        return True
    top=int(n**0.5)+1
    for i in range(2,top):   #判断在2到平方根内有无其他因数，有则返回失败
        if n%i==0:
            return False
    return True
def func_30():
    #输入指定数字内的所有质数
    n=int(input('Please input the number of numbers：'))
    for i in range(1,n):
        if is_prime(i):
            print(i,end=' ')
def func_31():
    #求S=a+aa+aa...a
    a=input('a=')
    n=int(input('n='))
    s=0
    for i in range(1,1+n):
        s+=int(a*i)       #先将字符个数累加，然后转化为整数加到总和里去
    print(s)
def func_32():
    #对给决定框架矩阵赋值，并且计算矩阵相加
    n=int(input('Please input the number of rows：'))
    m=int(input('Please input the number of columns：'))
    import numpy as np
    A=np.zeros((n,m))   #生成n行m列A矩阵
    B=np.zeros((n,m))   #生成n行m列B矩阵
    for i in range(n):
        for j in range(m):
            A[i][j]=int(input('Please input A[{},{}]:'.format(i,j))) #对A矩阵赋值
    for i in range(n):
        for j in range(m):
            B[i][j]=int(input('Please input B[{},{}]:'.format(i,j))) #对B矩阵赋值
    print('c=',A+B)   #矩阵相加为C
def main():
    #func_26()
    #func_27()
    #func_28()
    #func_29()
    #func_30()
    #func_31()
    func_32()
    pass
if __name__=='__main__':
    main()
