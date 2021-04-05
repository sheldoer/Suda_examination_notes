def _2012():
    """
    **程序：**
    `2012`年复试上机题
    **要求：**
    * 从服务器上下载数据文件`org.dat`文件以二进制方式存放一系列整数，每个整数占`4`个字节.
    从第一个整数开始，第一个整数和第二个整数构成一个坐标点，以此类推，数据文件中保存了许多坐标点数据.
    * 规定处于第一象限的坐标点为有效点，请问数据文件中所有点的个数`n`为多少？有效点的个数`k`为多少？
    * 每个有效点与坐标原点构成一个的矩形，请问`k`个有效点与坐标原点构成的`k`个矩形的最小公共区域面积为多少？
    * 寻找有效点钟符合下列条件的点：以该点为坐标原点，其它有效点仍然是有效点即处于第一象限
    (不包括坐标轴上的点).输出这些点.
    * 对所有有效点进行分组，每个有效点有且只有属于一个分组，分组内的点符合下列规则：
    若对组内所有点的x坐标进行排序，点`p1(x1, y1)`在点`p2(x2, y2)`后面，即`x1>x2`那么`y1>y2`，请输出所有的分组.
    """

    def read_from_file():
        with open('org.dat', 'rb') as file:
            s = file.read().decode()
        length = len(s) // 8
        points_p = [(int(s[i * 8:i * 8 + 4]), int(s[i * 8 + 4:i * 8 + 8])) for i in range(length)]
        one_area_p = [t for t in points_p if t[0] > 0 and t[1] > 0]
        one_area_p.sort(key=lambda k: k[0])
        return points_p, one_area_p

    def get_area(m):
        return m[0] * m[1]

    def group(points_c: list):
        result = [[points_c[0]]]
        p = 0
        pre = points_c[0][1]
        for i, j in points_c[1:]:
            if j > pre:
                result[p].append((i, j))
            else:
                result.append([(i, j)])
                p += 1
            pre = j
        return result

    def out_group(p):
        for i in p:
            for c in i:
                print(c, end=',')
            print("")

    points, one_area = read_from_file()
    min = get_area(one_area[0])
    for point in one_area:
        this_area = get_area(point)
        if this_area < min:
            min = this_area
    print('面积最小:{}'.format(min))

    if one_area[0][1] < one_area[1][1]:
        print('这个点是:({},{})'.format(one_area[0][0], one_area[0][1]))
    else:
        print('不存在这种点')

    out_group(group(one_area))
_2012()
