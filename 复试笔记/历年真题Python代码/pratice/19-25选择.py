from sympy import *
def func_19():
    #对二次函数进行求解
    a,b,c=list(map(float,eval(input('a,b,c:')))) #依次输入a,b,c
    if a==0:                      #如果a为0，则无意义
        print('该函数无意义')
    else:                           #不为0时，求解方程
        x=Symbol('x')
        d1=(a*x**2+b*x+c)-(0)
        print(solve([d1]))
def func_20():
    #判断三个点围成图形的周长及面积，并且判断是否为三角形
    x1,x2,x3,y1,y2,y3=list(map(float,eval(input('x1,x2,x3,y1,y2,y3:'))))#输入3个点的6个坐标
    f=lambda a1,a2,b1,b2:((a1-a2)**2+(b1-b2)**2)**0.5 #求两点线段长函数f
    l1=f(x1,x2,y1,y2)
    l2=f(x1,x3,y1,y3)
    l3=f(x2,x3,y2,y3)
    t=(l1+l2+l3)/2
    if max(l1,l2,l3)==t:      #判断最长边是否为周长的一半,如果是，则为直线
        print('该图形不是三角形，是直线')
    else:
        s=((t*(t-l1)*(t-l2)*(t-l3))**0.5) #根据公式求面积
        print('周长为:%f,面积为:%f'%(2*t,s))
def func_21():
    #判断一个点与一个圆的关系
    x1,y1,r,x2,y2=list(map(float,eval(input('x1,y1,r,y1,y2:'))))
    f=lambda a1,a2,b1,b2:((a1-a2)**2+(b1-b2)**2)**0.5 #求两点线段长函数f
    l=f(x1,x2,y1,y2)               #l为该点到圆圆心的距离
    if l==r:
        print('在圆上')
    elif l>r:
        print('在圆外')
    else:
        print('在圆内')
def func_22():
    #对一串数字进行顺序逆序输出
    x=input('请输入一个不多于5位的正整数:')
    rx=x[::-1]                    #将x逆置并存入rx中
    print('他是%d位数'%len(x))
    for i in x:                   #顺序输出
        print(i)
    for i in rx:                  #逆序输出
        print(i)

def func_23():
    #对三个整数根据从小到大输出
    res=list(map(int,eval(input('x,y,z;'))))
    res.sort()
    for i in res:
        print(i)
def func_24():
    #根据不同利息率计算利息
    x=eval(input('money:(万元)'))
    if x<10:
        print('%.4f万元'%(x*(1+0.015)))
    elif x>=10 and x<50:
        print('%.4f万元'%(x*(1+0.02)))
    elif x>=50 and x<100:
        print('%.4f万元'%(x*(1+0.03)))
    else:
        print('%.4f万元'%(x*(1+0.035)))
def func_25():
    #对字母进行转换输出
    x=input('请输入一个字母:') #将字母存入x
    if x<'z' and x>'a':        #x为小写字母
        print(x.upper())
    elif x>'A' and x<'Z':      #x为大写字母
        print(x.lower())
    else:                      #其他情况
        print(x)
def main():
    #func_19()
    #func_20()
    #func_21()
    #func_22()
    #func_23()
    #func_24()
    func_25()
    pass
if __name__=='__main__':
    main()
