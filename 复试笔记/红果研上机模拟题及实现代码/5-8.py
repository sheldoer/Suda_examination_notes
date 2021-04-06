def _5():
    from random import randint
    num=str(randint(1000,10000))
    print(num)
    print(num[::-1])

def _6():
    import time
    lt=time.localtime(time.time())
    print("当前时间是：%d:%d:%d"%(lt.tm_hour,lt.tm_min,lt.tm_sec))

def _7():
    import math
    h=int(input("请输入桶的高度:(cm)"))/100
    r=int(input("请输入桶的半径:(cm)"))/100
    v=h*math.pi*r**2
    num=20/v
    print("大象要喝%d桶水"%(num if num==int(num) else num+1))

def _8():
    import random
    import math
    r=random.randint(5,20)
    print('球的半径是：%-15.3f,球的体积是：%-15.3f'%(r,4/3*math.pi*r**3))
def main():
    pass
if __name__=='__main__':
    main()

    
    
