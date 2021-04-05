import struct
from random import randint
def read_file():
    #读取data里面的二进制文件
    with open("data.txt",'rb')as fp:
        size=struct.calcsize('i')
        f=fp.read(size)
        nums=[]
        while f:
            num=struct.unpack('i',f)[0]
            nums.append(num)
            f=fp.read(size)
    fp.close()
    #print(nums)
    return nums

def is_prime(n):
    #检测数字n是否为素数
    if n<2:
        return False
    if n==2:
        return True
    edg=int(n**0.5)+1
    for i in range(2,edg):
        if n%i==0:
            return False
    return True

def implement(nums:list):
    #实现函数
    nums.sort(reverse=True)
    n=len(nums)-nums.count(0)
    print('非零数的个数为:%d'%n)
    nums=nums[0:n]
    print("最大的数为:%d，最小的数为:%d"%(nums[0],nums[n-1]))
    for i in nums:
        if is_prime(i):
            print("最大的素数为:%d"%i)
            break
    s=int(n/3 if n/3==int(n/3) else n/3+1) #s代表每一段的个数
    print("中间段的最大数为:%d，最小数为:%d"%(nums[s],nums[2*s-1]))
    
def main():
    
    #生成二进制文件
    with open('data.txt','wb')as fq:
        for i in range(2048):
            num=struct.pack('i',randint(0,80))
            fq.write(num)
    fq.close()
    
    nums=read_file()
    implement(nums)
    
if __name__=='__main__':
    main()
