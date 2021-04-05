import struct
from random import randint
"""
    ##### `2015`年复试上机
    **要求：**
    * 从网页上下载`input.dat`文件，里面是用二进制编写的，里面放了一堆`int`型的数，
    每个数占`4`个字节，每次读取两个，这两个数构成一个坐标.
    * 规定处于第一象限的数是有效点(即`x>0, y>0`的坐标)，问这么多点中有效点有多少个？
    * 从键盘上输入`k`和`n`，从第一问中的有效点中找出距离小于`n`，距离小于`n`的点的个数要大于`k`，
    将它们以文本格式输出到文件中.
    **程序：**
    """
def read_file():
    #读取二进制文件，并且把读取的数字存储到point列表中
    with open("input.txt","rb")as fp:
        size=struct.calcsize('i')
        f=fp.read(size)
        point=[]
        while f:
            value=struct.unpack('i',f)[0]
            point.append(value)
            f=fp.read(size)
    return point

def make_coord(point:list):
    #根据数字列表进行两两组合，形成coords的点集合
    size=len(point)//2
    coords=[]
    for i in range(size):
        p=[point[2*i],point[2*i+1]]
        coords.append(p)
    return coords

def available_point(coords:list,n:float,k:int):
    #统计有效点个数，并且在有效点集合里找到符合要求的点存储到out.txt里
    fq=open("out.txt",'w')
    avail=[]
    for i in coords:
        if i[0]>0 and i[1]>0:
            avail.append(i)
    for i in avail:
        count=0
        for j in avail:
            if i!=j and (i[0]-j[0])**2+(i[1]-j[1])**2<n**2:
                count+=1
        if count>k:
            print(i[0],i[1])
            fq.write('('+str(i[0])+','+str(i[1])+')\n')
    fq.close()
    return len(avail)             
    
def main():
    '''
    #生成二进制数字文件
    with open("input.txt","wb")as fp:
        for i in range(100):
            data=struct.pack('i',randint(-5,100))
            fp.write(data)
    '''
    points=read_file()
    coords=make_coord(points)
    n=float(input("请输入距离n值:"))
    k=int(input("请输入个数要求k:"))
    print(available_point(coords,n,k))
    
if __name__=="__main__":
    main()
