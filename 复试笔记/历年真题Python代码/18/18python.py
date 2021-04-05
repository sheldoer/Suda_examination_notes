from random import randint
import struct
"""
  在20000个数中找一个满足下列条件的最大集合：
  集合中所有数之间的最大公因数是1（即两两互质）
  :param arr:
  :return:
  """


def prime_num(n):
    #查找n的因子
    num = set()
    i = 2
    while i <= n:
        if n % i == 0:
            num.add(i)
            n = int(n/i)
        else:
            i += 1
    return num


def prime_num2(n):
    num = set()
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                num.add(i)     #如果有小因子，则添加到因子集合里去
                n = int(n/i)
                break
    return num


def find_list():
    with open("input.txt", "rb")as fp:  #读二进制文件
        size = struct.calcsize('i')
        f = fp.read(size)
        point = []
        while f:
            value = struct.unpack('i', f)[0]
            point.append(value)
            f = fp.read(size)
    point = sorted(set(point))                    #将读取的数字进行从小到大排序
    #print(point)
    factors = set()                               #建立已存在的因子集合
    res = []                                      #存储目标数字集合
    for i in point:
        num = prime_num(i)                        #求出每个数字的因子序列
        if num & factors:                         #如果已存在因子，则舍弃该数字
            continue
        else:
            res.append(i)
            factors = factors | num
    return res


'''
    with open("input.txt", "wb")as fp:
        for i in range(20):
            data = struct.pack('i', randint(-5, 100))
            fp.write(data)
'''


if __name__ == '__main__':
    print(find_list())
