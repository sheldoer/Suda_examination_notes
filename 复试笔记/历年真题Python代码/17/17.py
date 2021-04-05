def _2017():
    """
    `2017`年复试上机题
    **要求：**
    已知：二进制数据文件`data.bin`中存放了若干个整数，请编写程序完成如下功能：
    * 编写程序读取所有数据.
    * 以每相邻两个整数为一对按顺序构成二维平面上的坐标点. 例如：有数据`12`，`34`，`53`，`25`，`61`，`28`，`78`等，
    则构成六个坐标点如下：`(12, 34)`、`(34, 53)`，`(53, 25)`, `(25, 61)`, `(61, 28)`, `(28, 78)`；
    * 以每个坐标点为圆心，以该点与其后面第一个点的欧氏距离为半径`r`. 计算每个圆包含的坐标点数. 计
    算最后一个点时以其和第一个点的欧氏距离为半径.
      例如：
      坐标点`(12, 34)`的圆半径$r=\sqrt{(12-34)^2+(34-53)^2}$是坐标点`(12, 34)`与`(34, 53)`的欧式距离.
      坐标点`(28, 78)`的圆半径$r=\sqrt{(28-12)^2+(78-34)^2}$是坐标点`(28, 78)`与`(12, 34)`的欧式距离.
    * 计算所有圆的点密度值，然后输出点密度值最大的`5`个坐标点以及相应圆中包含的点数和点密度值. 输出格式要求：
      |     坐标点     |    包含点数     |            点密度            |
      | :------------: | :-------------: | :--------------------------: |
      | (x坐标，y坐标) | (占5列，右对齐) | (占7列，右对齐，保留2位小数) |
      上述文字部分不需要显示.
    其中：圆的点密度为圆包含的点数除以圆面积，如果点在圆上，则也算圆包含该点，在计算点密度时，圆心也算一个点. 计算圆面积时$\pi=3.14$.
    例如：坐标点`(2, 1)`，则该坐标点也属该坐标点的圆内的一个点.
    **程序：**
    :return:
    """

    def read_file():
        with open('data.txt', encoding='utf-8', mode='rt') as f:
            nums = f.read().split()
        nums = list(map(int, nums))
        size = len(nums)
        ans = []
        for i in range(size):
            if i + 1 < size:
                point = [nums[i], nums[i + 1]]
            else:
                break
            ans.append(point)
        return ans

    def compute_radius(ls: list):
        ans = []
        for index, t_point in enumerate(ls):
            x, y = t_point[0], t_point[1]
            next = index + 1
            if next >= len(ls):
                next = 0
            point = ls[next]
            r = ((x - point[0]) ** 2 + (y - point[1]) ** 2) ** 0.5
            ans.append([x, y, r])
        return ans

    def count_inner(point: list, points: list):
        import math
        c = 0
        for x, y, r in points:
            d = ((x - point[0]) ** 2 + (y - point[1]) ** 2) ** 0.5
            if d <= point[2]:
                c += 1
        s = math.pi * point[2] * point[2]
        md = c / s
        return c, md

    def computer_md(ls: list):
        ans = []
        for point in ls:
            c, md = count_inner(point, ls)
            ans.append([point[0], point[1], c, md])
        return ans

    def print_result(ls: list):
        for x, y, c, md in ls:
            print('({0}, {1}) {2:>5} {3:>7.7f}'.format(x, y, c, md))

    def main():
        arr = read_file()
        arr_and_r = compute_radius(arr)
        ls = computer_md(arr_and_r)
        ls.sort(key=lambda x: x[3], reverse=True)
        print_result(ls[:5])

    main()
_2017()
