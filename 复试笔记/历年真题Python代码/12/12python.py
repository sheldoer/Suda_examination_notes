import struct
from random import randint
def read_file():
    with open("org.dat",'rb')as fp:
        size=struct.calcsize('i')
        f=fp.read(size)
        nums=[]
        while f:
            num=struct.unpack('i',f)[0]
            nums.append(num)
            f=fp.read(size)
    fp.close()
    return nums
def make_site(nums:list):
    n=len(nums)//2
    ava=[]
    for i in range(n):
        if nums[i*2]>0 and nums[2*i+1]>0:
            ava.append([nums[2*i],nums[2*i+1]])
    print(ava)
    return n,ava
def min_s(ava:list):
    minx=100
    miny=100
    for i,j in ava:
        if i<minx:
            minx=i
        if j<miny:
            miny=j
    return minx*miny
    
def main():
    '''
    with open("org.dat",'wb')as fp:
        for i in range(100):
            fp.write(struct.pack('i',randint(-5,100)))
    fp.close()
    '''
    nums=read_file()
    n,ava=make_site(nums)
    print("文件中所有点个数n为：%d,有效点个数k为:%d"%(n,len(ava)))
    print("最小的公共区域面积为:%d"%min_s(ava))
    
if __name__=="__main__":
    main()
