def _by_2017():
    """
    ##### `2017`年保研上机题
    **要求：**
    文本文件`input.txt`里面放了一堆整数，仅仅以空格分隔，
    其中第一个整数为`k`，第二个整数代表维度，剩余的整数作为点的坐标.
    要求：
    * 读取整数`k`和维度，并读取剩余的整数组成指定维度的点.
    * 从所有点中找到距离最近的两个点并输出它们的坐标和距离.
    * 分别输出距离这两个点最近的`k`个点的坐标 .
    **程序：**
    """

    def read_file():
        with open('input.txt', encoding='utf-8') as file:
            data = file.read().split()
            data = list(map(int, data))
        if len(data) < 2:
            return None
        k = data.pop(0)
        dimension = data.pop(0)
        size = len(data) // dimension
        points = []
        for i in range(size):
            point = []
            for j in range(dimension * i, dimension * (i + 1)):
                if j >= len(data):
                    break
                point.append(int(data[j]))
            points.append(point)
        print('last point: {}'.format(points[-1]))
        return k, dimension, points

    def count_distance(a, b):
        su = 0
        for i in range(len(a)):
            x, y = a[i], b[i]
            su += abs(x - y) ** 2
        return su

    def point_print(point):
        k = list(map(str, point))
        return ','.join(k)

    def find_close(points):
        length = len(points)
        p1, p2 = points[0], points[1]
        min_distance = count_distance(p1, p2)
        for i in range(length):
            for j in range(i + 1, length):
                d = count_distance(points[i], points[j])
                if d < min_distance:
                    min_distance = d
                    p1, p2 = i, j
        print('p1=({}), p2=({}) distance = {:.2f}'.format(point_print(points[p1]), point_print(points[p2]),
                                                          min_distance ** 0.5))
        return p1, p2

    def get_nearest(p, data_o: list, k):
        data = sorted(data_o, key=lambda x: count_distance(data_o[p], x))
        return data[1:k + 1]

    def main():
        K, dimension, data_m = read_file()
        print('k={}, dimension={}'.format(K, dimension))
        point_a, point_b = find_close(data_m)
        ls_a, ls_b = get_nearest(point_a, data_m, K), get_nearest(point_b, data_m, K)
        point_a, point_b = data_m[point_a], data_m[point_b]
        print('the nearest {} points to point({}) is:'.format(K, point_print(point_a)))
        for p in ls_a:
            print('({})'.format(point_print(p)), end=' ')
        print()
        print('the nearest {} points to point({}) is:'.format(K, point_print(point_b)))
        for p in ls_b:
            print('({})'.format(point_print(p)), end=' ')

    main()
