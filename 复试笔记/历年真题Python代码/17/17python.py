def read_file():
    #读取data数据，每相邻的两个整数保存到point列表里
    with open('data.txt', 'r')as file:
        nums = file.read().split()
    num = list(map(int, nums))
    size = len(num)
    point = []
    for i in range(size-1):
        point.append([num[i], num[i+1]])
    return point


def coverage(point: list):
    #对每个点进行计算与下一个点的欧氏距离，将r的平方保存到point每个点的列表里
    seize = len(point)
    f = lambda x, y: (x[0]-y[0])**2+(x[1]-y[1])**2
    for i in range(seize-1):
        r2 = f(point[i], point[i+1])
        point[i].append(r2)
    r2 = f(point[seize-1], point[0])
    point[seize-1].append(r2)
    for i in point:
        #计算每个点覆盖点数，用n来计数
        n = 0
        for j in point:
            if f(i, j) <= i[2]:
                n += 1
        i.append(n)
    return point


def print_result(point: list):
    #先将point列表进行更新，将r的平方替换为点密度，根据点密度进行排序，输出前五个
    for i in point:
        i[2] = i[3]/i[2]/3.14
    point.sort(key=lambda x: x[2], reverse=True)
    for i in range(5):
        print('(%d,%d)%5d%7.2f' % (point[i][0], point[i][1], point[i][3], point[i][2]))


def main():
    point = read_file()
    point = coverage(point)
    print_result(point)


if __name__ == "__main__":
    main()
