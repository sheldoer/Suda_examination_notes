import math
import random


def read_file():
    # (1)编写函数read_file从文件中读取数据，将所有的整数按照其在文件中出现的顺序依次存储到数组arr中；
    with open("data.txt", 'r') as fp:
        arr = fp.read().split()
    return list(map(int, arr))


def arr_print(arr: list, n):
    #(2)编写函数print将数组arr显示在屏幕上，每行显示n个数，每个整数占6列；
    length = len(arr)
    size = length // n+1
    for i in range(size):
        for j in range(i * n, (i + 1) * n):
            if j < length:
                print('{:<6}'.format(arr[j]), end='')
        print()


def count(arr):
    #(3)编写函数count统计数字0至9在数组arr所有整数中的出现次数，将结果放入数组res中（即res[0]存储数字0的出现次数，res[1]存储数字1的出现次数，其余以此类推）；
    s = ''.join(list(map(str, arr)))
    res = [s.count(str(i)) for i in range(10)]
    return res


def print_res(res):
    #(4)编写函数print_res将数组res显示在屏幕上，每行显示5个数，可以复用步骤(2)中print函数；
    print_file(res, 5)


def sort_array(arr):
    #(5)编写函数sort_array将数组arr中的整数按照因子和从小到大排序，如果两个整数的因子和相等，则按照它们的自然大小排序（注意：计算一个整数的因子和时包括1和其本身）；
    return sorted(arr)


def filter_array(arr):
    # (6)编写函数filter_array对数组arr中的整数进行筛选，结果继续保存在arr中，筛选规则如下：保留所有的偶数，
    #    同时保证这些偶数按照从小到大排序。说明：完成筛选之后，数组arr中的元素可以分成两部分，前半部分是有效内容，
    #    即所有的偶数，后半部分则是无效内容，参数size记录了数组arr中有效内容的长度（注意：筛选要求在原数组上进行，
    #    如使用新的辅助数组来完成筛选，扣10分）；
    arr.sort()
    size = 0
    for i in range(0, len(arr)-1):
        if arr[i] != 0 and arr[i] % 2 == 0:
            num = arr[size]
            arr[size] = arr[i]
            arr[i] = num
            size += 1
    return size


def filter_array2(arr):
    #(6).2
    arr = list(filter(lambda x: x % 2 == 0, ar))
    arr.sort()
    return len(arr), arr


def is_prime(n):
    #判断数字n是否为质数
    edg = int(math.sqrt(n))+1
    for i in range(2, edg):
        if n % i == 0:
            return i
    return False


def write_file(arr, size):
    #(7)编写函数write_file对数组arr中的有效内容（即所有偶数）进行质因数分解，并将结果输出到屏幕和文本文件output.txt中。输出要求：每一个整数的质因数分解结果占一行，具体显示格式如下图所示：
    print(arr)
    with open("output.txt", 'w')as sq:
        for i in range(0, size):
            new = is_prime(arr[i])
            while new:
                sq.write(str(new)+'*')
                arr[i] = arr[i]/new
                new = isprime(arr[i])
            sq.write(str(int(arr[i]))+'\n')


def main():
    #主函数
    with open("data.txt", 'w') as fp:
        for i in range(0, 100):
            fp.write(str(random.randint(0, 32768))+'\n')
    arr = read_file()
    print_file(arr, 10)
    res = count(arr)
    print_res(res)
    sort_array(arr)
    size = filter_array(arr)
    write_file(arr, size)


if __name__ == '__main__':
    main()
