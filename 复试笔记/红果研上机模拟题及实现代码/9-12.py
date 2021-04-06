from random import randint
import math
import numpy as np
import time
def func_9():
    #求三角形面积
    x1,y1,x2,y2,x3,y3=eval(input('Please input six numbers:'))#三个点的横纵坐标
    f=lambda a,b,c,d:((a-c)**2+(b-d)**2)**0.5 #求边长公式
    l1=f(x1,y1,x2,y2)
    l2=f(x2,y2,x3,y3)
    l3=f(x1,y1,x3,y3)
    t=(l1+l2+l3)/2
    print('三角形的面积s为：%-8.3f'%((t*(t-l1)*(t-l2)*(t-l3))**0.5))

def func10(n:int):
    #递归实现求n年的收益
    if n==0:
        return 0
    return (100+func10(n-1))*1.005
def func_10():
    #根据年份来求年利率
    N=int(input('请输入年份N:'))
    fund=func10(N)
    print('存款金额为:%.5f,收益率为%.2f%%'%(fund,fund/N))

def func_11():
    #计算复数的模与辐角
    n1=randint(10,50)
    n2=randint(10,50)
    mod=(n1**2+n2**2)**0.5
    ang=np.arctan(n2/n1)
    s=str(n1)+'+'+str(n2)+'i'
    print("复数为%7s,模为%7.2f,辐角为%7.2f"%(s,mod,ang))

def func_12():
    #
    tm=time.localtime(time.time())
    print('距1970年1月1日过去了%d天%d小时'%())   ########'''不会'''
    

def main():
    #func_9()
    #func_10()
    #func_11()
    pass
if __name__=='__main__':
    main()
