"""
    `2011`年复试上机题
    **要求：**
    输出`1000-9999`中满足以下条件的所有数：
    * 该数是素数.
    * 十位数和个位数组成的数是素数，百位数和个位数组成的数是素数.
    * 个位数和百位数组成的数是素数，个位数和十位数组成的数是素数. 比如`1991`，
    个位和十位组成的数就是`19`.
"""
def isprime(n):
    #判断n是否为素数
    edg=int(n**0.5)+1
    for i in range(2,edg):
        if n%i==0:
            return False
    return True
def isaccord(n):
    #判断n是否符合条件
    g,s,b=n%10,n//10%10,n//100%10         #g为个位数，s为十位数，b为百位数
    if isprime(s*10+g)and isprime(b*10+g)and isprime(g*10+b)and isprime(g*10+s):
        return True
    return False

def make_prime():
    #遍历1000—9999，找到符合条件的数，存入prime中
    prime=[]
    for i in range(1000,10000):
        if isprime(i) and isaccord(i):
            prime.append(i)
    return prime
def main():
    #主函数
    print(make_prime())
    
if __name__=="__main__":
    main()
