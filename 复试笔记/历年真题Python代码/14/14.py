def _2014():
    """
    ##### `2014`年复试上机题
    **要求：**
    * 从网页上下载`input.dat`文件，里面是用二进制编写的，里面放了一堆`int`型的数，每个数占`4`个字节，每次读取两个，
    这两个数构成一个坐标.
    * 规定处于第一象限的数是有效点(即`x>0, y>0`的坐标)，问这么多点中有效点有多少个？
    * 现在用户从键盘输入一个坐标和一个数字`k`，设计算法输出`k`个离该坐标距离最近的点的坐标和每个坐标到该点的距离，
    写入到`output.txt`文件中.
    **程序：**
    """

    def read_from():
        with open('input.txt', 'rt') as file:
            content = file.read().split()
            content = list(map(int, content))
        size = len(content) // 2
        res = []
        for i in range(size):
            points = []
            for j in range(i * 2, i * 2 + 2):
                points.append(content[j])
            res.append(points)
        return res

    def count(points: list):
        c = 0
        for x, y in points:
            if x > 0 and y > 0:
                c += 1
        return c

    def get_closet_k(k: int, point: list, ls: list):
        ls.sort(key=lambda p: (point[0] - p[0]) ** 2 + (point[1] - p[1]) ** 2)
        return ls[:k]

    ps = read_from()
    leagel = count(ps)
    print('n={}'.format(leagel))
    p = input('input point:').split()
    p = list(map(int, p))
    k = eval(input('input k:'))
    points = get_closet_k(k, p, ps)
    line = []
    for po in points:
        d = ((po[0] - p[0]) ** 2 + (po[1] - p[1]) ** 2) ** 0.5
        line.append('({}, {}) distance={:.2f}'.format(po[0], p[1], d))
    with open('Output.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(line))
