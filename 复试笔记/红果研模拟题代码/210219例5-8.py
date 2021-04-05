import math
def Isprime(n):
    m=int(math.sqrt(n))+1
    #print(m)
    for i in range(2,m):
        if n%i==0:
            return False
    return True
def demo(n):
    if isinstance(n,int)and n>0 and n%2==0:
        for i in range(3,int(n/2)+1):
            if i%2==1 and Isprime(i) and Isprime(n-i):
                print(i,'+',n-i,'=',n)

demo(50)
