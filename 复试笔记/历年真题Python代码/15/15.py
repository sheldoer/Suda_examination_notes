import struct
def _2015():
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
    with open("input.txt","rb")as fp:
        size=struct.calcsize('i')
        f=fp.read(size)
        p=[]
        while f:
            value=struct.unpack('i',f)[0]
            p.append(value)
            f=fp.read(size)
    fp.close()
    '''
    with open('input.txt', encoding='utf-8') as f:
        p = f.read().split()
        p = list(map(int, p))
    '''
    size = len(p) // 2
    ans = []
    for i in range(size):
        point = []
        for j in range(i * 2, i * 2 + 2):
            point.append(p[j])
        ans.append(point)
    vaild = []
    for x, y in ans:
        if x > 0 and y > 0:
            vaild.append((x, y))
    print('vaild: {}'.format(len(vaild)))
    k = eval(input('input k: '))
    n = eval(input('input n: '))
    distance = {}
    for i in range(len(vaild)):
        px, py = vaild[i]
        for j in range(i + 1, len(vaild)):
            ppx, ppy = vaild[j]
            key = '{}{}{},{}{}{}'.format(i, px, py, j, ppx, ppy)
            key2 = '{}{}{},{}{}{}'.format(j, ppx, ppy, i, px, py)
            if distance.get(key):
                continue
            elif distance.get(key2):
                continue
            else:
                distance[key] = ((px - ppx) ** 2 + (py - ppy) ** 2) ** 0.5
    for i in range(len(vaild)):
        px, py = vaild[i]
        c = 0
        ls = []
        for j in range(len(vaild)):
            if j == i:
                continue
            ppx, ppy = vaild[j]
            key1 = '{}{}{},{}{}{}'.format(i, px, py, j, ppx, ppy)
            key2 = '{}{}{},{}{}{}'.format(j, ppx, ppy, i, px, py)
            d = distance.get(key1) if distance.get(key1) else distance.get(key2)
            if d < n:
                c += 1
                ls.append([vaild[j], d])
        if c <= k:
            continue
        print()
        print('distance less {} to point: ({}, {}) as follows:'.format(n, px, py))
        for point, d in ls:
            print('({}, {}), d={:.2f}'.format(point[0], point[1], d))
        print()
_2015()
