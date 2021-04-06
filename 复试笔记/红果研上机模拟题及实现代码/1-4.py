def _1():
    a=int(input("请输入正整数a："))
    b=int(input("请输入正整数b："))
    print( '商：',divmod(a,b)[0],
           '余数：',divmod(a,b)[1])

def _2():
    print(len(input("请输入一个中文词语:")))

def _3():
    m=int(input("请输入一个三位整数:"))
    num=0
    while m:
        m,n=divmod(m,10)
        num+=n
    print("%4d"%num)

def _4():
    nums=(input("请输入两个坐标点的横纵坐标:")).split()
    a,b,c,d=float(nums[0]),float(nums[1]),float(nums[2]),float(nums[3])
    print('两点的距离：',((a-c)**2+(b-d)**2)**0.5)
