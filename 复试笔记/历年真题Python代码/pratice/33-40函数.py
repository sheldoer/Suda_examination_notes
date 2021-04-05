def func_33():
    #求一个整数的所有因子之和
    n=int(input('input a number:'))   #输入整数
    ls=set()                           #创建一个空集合
    for i in range(1,n):
        if n%i==0:                   #将可以除尽的因子添加到集合中
            ls.add(i)
    print(sum(ls))
def func_34():
    #将数字逆置
    n=int(input('input a number:'))   #输入整数
    print('the reverse is:{}'.format(int(str(n)[::-1]))) #将数字转化为字符串逆置后再转化为数字
def is_prime(n):
    #判断n是否为素数
    if n<2:
        return False
    if n==2:
        return True
    top=int(n**0.5)+1        #判断的上界
    for  i in range(2,top):
        if n%i==0:           #如果能被任意一位小的数整除，则不为素数
            return False
    return True
def is_pal(n):
    #判断n是否为回文数
    if int(str(n)[::-1])==n:
        return True
    else:
        return False
def func_35():
    #依次输出8个数，总共输出30个数
    coun=0           #coun用来计数
    num=0            #num代表遍历的每一个数
    res=[]           #res用来存储条件符合的数字
    while coun<30:
        if is_prime(num) and not is_pal(num):  #找到适合条件的反素数
            res.append(num)
            coun+=1
        num+=1
    for i in range(coun//8+1):        #按条件输出
        for j in range(8):
            if i*8+j<coun:
                print('{:5}'.format(res[i*8+j]),end='')
        print()
def is_pars(n):
    #判断n是否为帕森素数
    if is_prime(n):
        p=0
        n=n+1       #先将n加一，再累除2
        while n%2==0:
            n/=2
            p+=1
        if n==1:    #如果能除为1，则说明是，并返回p
            return p
    return -1
def func_36():
    #寻找1000以内的帕森素数
    res=[]   #存储符合条件的帕森素数
    for i in range(1000):
        p=is_pars(i)    #先求出经函数判断的p值
        if p!=-1:        #如果是帕森素数，则依次存储p和该数
            re=[]
            re.append(p)
            re.append(i)
            res.append(re)
    for i,j in res:
        print('{:3}{:4}'.format(i,j))   #依照要求输出
def func_37():
    #
    s=input('input a string:')
    ms=''
    n=int(input('encode bite:'))
    import re
    nums=re.findall('\d+',s)
    for i in range(len(nums)):
        s=s.replace(nums[i],str(int(nums[i])*5))
    for i in s:
        if i>='A' and i<='Z':
            ms+=str(chr(ord('A')+(ord(i)-ord('A')+n)%26))
        elif i>='a' and i<='z':
            ms+=str(chr(ord('a')+(ord(i)-ord('a')+n)%26))
        else:
            ms+=i
    print('加密前的字符串：{}\n加密后的字符串：{}'.format(s,ms)) #####开始未作出
def func_38():
    #将给定的英文语句单词倒序
    s=input('input a string:')    #输入待倒序语句
    res=s.split()                 #依据空格分隔成列表
    rs=' '
    print(rs.join(res[::-1]))     #将倒序列表用空格链接
def func_39():
    #统计指定位置字符在字符串中出现的次数
    s=(input('input a string:')).lower()    #输入语句并转化为全小写
    n=int(input('input the index:'))        #输入待统计位置
    print(s.count(s[n]))                    #利用count函数统计
def Fibonacci(res,n):
    #做出斐波那契数列
    if len(res)<2:      #初始化前两位，分别为1，1
        res.append(1)
        res.append(1)
    if len(res)<n:       #递归出口
        res.append(res[-1]+res[-2])  #未到n，则继续生成数列
        return Fibonacci(res,n)
        #print(res)
    else:
        return res[-1]
def func_40():
    #利用递归得到斐波那契数列，然后输出指定项的值
    res=[]
    print(Fibonacci(res,9))
    
def main():
    #func_33()
    #func_34()
    #func_35()
    #func_36()
    func_37()
    #func_38()
    #func_39()
    #func_40()
    pass
if __name__=='__main__':
    main()
