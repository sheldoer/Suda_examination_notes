def make_prime(n):
    nums = [1] * n
    nums[0], nums[1] = 0, 0
    for i in range(2, n):
        if nums[i]:
            for j in range(i * i, n, i):
                nums[j] = 0
    return nums


def equal_prime(n):
    """
    `2005`年复试上机题
    把一个数表示成若干个素数的和.
    注， 此题不用这个方法。
    """

    def judge_prime(n):
        if n == 0 or n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        # 判断
        if 0 in [n % i for i in range(2, int(n ** 0.5 + 1))]:
            return False
        return True

    def DFS(n, index=0, sum=0, primes=[], L=[], S=None):
        if S is None:
            S = set()
        if (sum > n):
            return
        # sum==n 找到了这样的一组数字
        if index < len(primes):
            if sum == n:
                if tuple(L) not in S:  # 避免重复输出
                    print(L)
                    S.add(tuple(L))
            L.append(primes[index])
            DFS(n, index, sum + primes[index], primes, L, S)
            L.pop()
            DFS(n, index + 1, sum, primes, L, S)

    plist = [i for i in range(n + 1) if judge_prime(i)]
    DFS(n, 0, 0, plist, S=set())


def _count_():
    """
    2005
     ``统计篇文章中各英文字母的个数，并排序.
    """
    file = open("a.json", encoding='utf-8')
    txt = ''.join(file.readlines())
    file.close()
    dic = {}
    for c in txt:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            dic[c] = dic.get(c, 0) + 1
    ls = list(dic.items())
    ls.sort(key=lambda c: c[1])
    for i, j in ls:
        print("{} ：{} 次".format(i, j))


def _find_prime_excloud_9():
    """
    ##### `2006`年复试上机题
    **要求：**
    找出`100`到`1000`内的不含`9`的素数，存到`result`文件中.
    """

    def not_has_9(x):
        p = x
        while p:
            c = p % 10
            if c == 9:
                return False
            p = p // 10
        return True

    ls = make_prime(1000)
    res = [str(i) for i in range(100, 1000) if ls[i] and not_has_9(i)]
    file = open("_find_prime_excloud_9.txt", 'w', encoding='utf-8')
    file.write('\n'.join(res))
    file.close()


def find_prime():
    """
    ##### `2007`年复试上机题
    **要求：**
    把`10`到`1000`之间满足以下两个条件的数，存到`result.txt`文件中.
    * 是素数.
    * 它的反数也是素数，如：`123`的反数是`321`.
    **程序：**
    """

    def get_reverse(x):
        g, s, b = x % 10, x // 10 % 10, x // 100 % 10
        return g * 100 + s * 10 + b

    ls = make_prime(1000)
    for i in range(10, len(ls)):
        if ls[i] and ls[get_reverse(i)]:
            print(i)


def _read_word():
    """
    **要求：**
    * 用`IE`从`FTP`上下载`org.dat`，并保存在`D`盘的根目录中.
    * 此文件中按文本方式存放了一段其他文章，其中有若干长度小于`15`的英文单词，单词之间用空格分开，无其他符号.
    * 顺序读取这段文章的不同的单词(大小写敏感)，同时在读取的过程中排除所有的单词`THE`以及变形，即这些单词不能出现在读取的结果中.
    * 将读取的所有单词的首字母转大写后，输出`D`根目录下`new.txt`，每个单词一行.
    **程序：**
    """
    source = open('D:/org.dat', encoding='utf-8')
    words = [x.title() for x in ' '.join(source.readlines()).split()]
    source.close()
    word_times = {}
    file = open('D:/new.txt', 'a', encoding='utf-8')
    for word in words:
        if word == 'The':
            continue
        if word_times.get(word):
            continue
        word_times[word] = word_times.get(word, 0) + 1
        file.writelines(word + '\n')
    file.close()


def _to_num():
    """
     `2009`年复试上机题
    **要求：**
    * 用`IE`浏览器从`FTP`上下载`org.dat`，并保存在`D`盘的根目录下.
    * 此文件中按文本方式存放了一段其他文章，其中有若干长度小于`15`的十进制或八进制数字，数字之间用`,`分开，数字内部存在且仅存在空格.
    * 八进制数以起始位`0`作为标示与十进制数区分.
    * 顺序读取这些数字将他们转变为十进制数后按从大到小的顺序排序后，输出到`D`盘根目录下`new.txt`，每个数字一行.
      `eg`：`_235_,34__2,_043_1_,1_3`，分别是：十进制`235`，十进制`342`，八进制`431`，十进制`13`，`_`代表空格.
    **程序：**
    """
    source = open('D:/org.dat', encoding='utf-8')
    words = [x.strip() for x in ','.join(source.readlines()).split(',')]
    source.close()
    ans = []
    for word in words:
        word = word.replace(' ', '')
        if word[0] == '0':
            n = '0o' + word[1:]
            ans.append(str(eval(n)))
        else:
            ans.append(word)
    file = open('D:/new.txt', 'w', encoding='utf-8')
    file.write('\n'.join(ans))
    file.close()


def _count_n():
    """
     `2010`年复试上机题
    **要求：**
    * 从`FTP`上下载`make.exe`和`org.dat`，运行`make.exe`输入准考证后三位生成`data.txt`，文件为二进制编码.
    * `data.txt`内存有`2048`个整数，其中前`n`个为非`0`数，后`2048-n`个数为`0`，将其读入数组，计算非零数的个数`n`.
    * 选出`n`个数中的最大数和最小数.
    * 选出`n`个数中最大素数.
    * 将`n`个数从大到小排序，并平均分成三段(若`n`非`3`的整数倍，则不考虑最后的`1-2`个数)，选出中间段的最大数和最小数.
    **程序：**
    """

    def receive_data():
        file = open('data.txt', 'rb')
        source = list(map(int, file.read().decode().split()))
        file.close()
        for i in range(len(source) - 1, -1, -1):
            if source[i] != '0':
                break
            else:
                del source[i]
        source.sort(reverse=True)
        return source

    def is_prime(x):
        if x == 1:
            return False
        if x == 2:
            return True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    source = receive_data()
    print('n = {}'.format(len(source)))
    print('max = {} min = {}'.format(source[0], source[-1]))
    for i in source:
        if is_prime(i):
            print('max_prime = {}'.format(i))
            break
    r = len(source) // 3
    print('中间段的最大值为：{}'.format(source[r]))


def print_1000_9999():
    """
    `2011`年复试上机题
    **要求：**
    输出`1000-9999`中满足以下条件的所有数：
    * 该数是素数.
    * 十位数和个位数组成的数是素数，百位数和个位数组成的数是素数.
    * 个位数和百位数组成的数是素数，个位数和十位数组成的数是素数. 比如`1991`，个位和十位组成的数就是`19`.
    """
    data = make_prime(10000)

    def getF4(n):
        g, s, b = n % 10, n // 10 % 10, n // 100 % 10
        return g * 10 + s, s * 10 + g, g * 10 + b, b * 10 + g

    for i in range(1000, 10000):
        if data[i]:
            ls = getF4(i)
            for c in ls:
                if not data[c]:
                    break
            else:
                print(i)


def _2012():
    """
    **程序：**
    `2012`年复试上机题
    **要求：**
    * 从服务器上下载数据文件`org.dat`文件以二进制方式存放一系列整数，每个整数占`4`个字节. 从第一个整数开始，第一个整数和第二个整数构成一个坐标点，以此类推，数据文件中保存了许多坐标点数据.
    * 规定处于第一象限的坐标点为有效点，请问数据文件中所有点的个数`n`为多少？有效点的个数`k`为多少？
    * 每个有效点与坐标原点构成一个的矩形，请问`k`个有效点与坐标原点构成的`k`个矩形的最小公共区域面积为多少？
    * 寻找有效点钟符合下列条件的点：以该点为坐标原点，其它有效点仍然是有效点即处于第一象限(不包括坐标轴上的点). 输出这些点.
    * 对所有有效点进行分组，每个有效点有且只有属于一个分组，分组内的点符合下列规则：若对组内所有点的x坐标进行排序，点`p1(x1, y1)`在点`p2(x2, y2)`后面，即`x1>x2`那么`y1>y2`，请输出所有的分组.
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


def _2013():
    """
    `2013`年复试上机题
    **要求：**
    * **Introduction**
      The project will read flight data from an input file and flight path requests from another input file
      and output the required information.
    * **Your Task**
      Your program should determine ***if a particular destination airport can be reached from
      a particular originating airport within a particular number of hops.
    ***
      A hop (leg of a flight) is a flight from one airport to another on the path between
      an originating and destination airports.
      For example, the flight plan from `PVG` to `PEK` might be `PVG -> CAN -> PEK`.
      So `PVG -> CAN` would be a hop and `CAN -> PEK` would be a hop.
    * **Input Data Files**
      * Path Input File(`PathInput.txt`)

        This input file will consist of a number of single origination/destination airport pairs
         (direct flights).The first line of the file will contain an integer representing the total
         number of pairs in the rest of the file.
        ```
        6
        [PVG, CAN]
        [CAN, PEK]
        [PVG, CTU]
        [CTU, DLC]
        [DLC, HAK]
        [HAK, LXA]
        ```
      * Path Request File(`PathRequest.txt`)
        This input file will contain a sequence of pairs of origination/destination airports and
        a max number of hops. The first line of the file will contain an integer representing the
        number of pairs in the file.
        ```
        2
        [PVG, DLC, 2]
        [PVG, LXA, 2]
        ```
      * Output File(`Output.txt`)
        For each pair in the Path Request File, your program should output
        the pair followed by `YES` or `NO` indicating that it is possible
        to get from the origination to destination airports within the max number
        of hops or it is not possible, respectively.
        ```
        [PVG, DLC, YES]
        [PVG, LXA, NO]
        ```
      * **Assumptions you can make:**
      You may make the following simplifying assumptions in your project:
      * `C/C++` is allowed to be used.
      * All airport codes will be `3` letters and will be in all caps
      * Origination/destination pairs are unidirectional. To indicate that both directions
      of flight are possible, two entries would appear in the file. For example,
      `[PVG, PEK]` and `[PEK, PVG]` would have to be present in the file to indicate
      that one could fly from `Shanghai` to `Beijing` and from `Beijing` to `Shanghai`.
      **程序：**
    """

    def read_file():
        with open('PathInput.txt') as file:
            content = file.read().split('\n')
        with open('PathRequest.txt') as file:
            request = file.read().split('\n')
        path, req = [], []
        for i in content[1:]:
            if i:
                a, b = list(map(lambda x: x.strip(), i.strip(' []').split(',')))
                path.append((a, b))
        for i in request[1:]:
            if i:
                a, b, c = list(map(lambda x: x.strip(), i.strip(' []').split(',')))
                req.append((a, b, int(c)))
        return path, req

    def create_map(data: list):
        dic = {}
        for a, b in data:
            dic[a] = dic.get(a, [])
            dic.get(a).append((b))
        return dic

    def init_visit(data: list):
        visit = {}
        for a, b in data:
            visit[a] = 0
            visit[b] = 0
        return visit

    def dfs(visit: dict, graph: dict, start: str, end: str, deep: int):
        if deep == 0:
            return False
        if start == end:
            return True
        ls = graph.get(start)
        print(start, deep)
        visit[start] = 1
        if ls:
            for item in ls:
                if visit[item] == 0 and dfs(visit, graph, item, end, deep - 1):
                    return True
        return False

    def write_to_file(ls):
        with open('Output.txt', 'w') as file:
            file.write('\n'.join(ls))

    city_sites, require_path = read_file()
    map_c = create_map(city_sites)
    answer = []
    for start, end, hops in require_path:
        visited = init_visit(city_sites)
        flag = dfs(visited, map_c, start, end, hops + 1)
        result = '[{}, {}, {}]'.format(start, end, 'Yes' if flag else 'No')
        answer.append(result)
    write_to_file(answer)


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


def _2015():
    """
    ##### `2015`年复试上机
    **要求：**
    * 从网页上下载`input.dat`文件，里面是用二进制编写的，里面放了一堆`int`型的数，每个数占`4`个字节，每次读取两个，这两个数构成一个坐标.
    * 规定处于第一象限的数是有效点(即`x>0, y>0`的坐标)，问这么多点中有效点有多少个？
    * 从键盘上输入`k`和`n`，从第一问中的有效点中找出距离小于`n`，距离小于`n`的点的个数要大于`k`，将它们以文本格式输出到文件中.
    **程序：**
    """
    with open('input.txt', encoding='utf-8') as f:
        p = f.read().split()
        p = list(map(int, p))
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


def _2016():
    """
     `2016`年复试上机题
    **要求：**
    文本文件`input.txt`由若干英文单词和分隔符(空格，回车，换行)构成. 根据如下说明编写程序统计不同单词出现的次数(频度).
    将统计结果按出现频度从高到低排序，并将出现频度大于`5`的单词及其频度输出到文件`output.txt`中. 文件格式如图所示
    ![format](E:\Markdown\img\format.png)
    * 多个连续的分隔符被视为一个分隔符.
    * 大小写敏感.
    * 每个单词的长度不超过`20`个字符.
    * 单词的数量未知. 如使用定义静态大数组的方式来统计，将被扣除`5`分.
    **程序：**
    :return:
    """
    file = open('input.txt', encoding='utf-8')
    txt = file.read()
    file.close()
    import re
    res = re.split(r'\s+', txt)
    print(res)
    dic = {}
    for word in res:
        dic[word] = dic.get(word, 0) + 1
    ans = []
    for k in dic:
        if dic.get(k) > 5:
            ans.append('{}: {}'.format(k, dic.get(k)))
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(ans))


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
        with open('input.txt', encoding='utf-8', mode='rt') as f:
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


def _by_2016():
    """
    ##### `2016`年保研上机题
    ** 要求： **
    *请从服务器将两个数据文件 `input.txt` 和 `words.txt`   下载到本地电脑的 `D`  盘根文件夹。
    *在  `D`  盘根文件夹的  `words.txt`  中存储了不超过  `30000`条的英文单词，每个单词占一行。单词的最大长度为`20`，
    且单词内部没有空格，文件中无重复单词。
    *在D盘根文件夹的 `input.txt` 中存储了一个「丢失」了空格和标点符号的英文文章。每行不超过 `128`个字符，请编写程序把
    该文章中第一行和最后一行显示在屏幕上。
     *编写程序将 `words.txt`中的最后三行显示在屏幕上； *编写程序利用 `words.txt`    中的单词作为词典，采用正向最大
     匹配切分单词算法对   `input.txt`    中的文本进行单词切分。切分时单词区分大小写， 切分分割标记采用空格，并将切分
     后的结果写入到`out.txt` 中。
    所谓正向最大匹配切分就是从左向右扫描待切分字符串，尽量取长词。 下面举一个简单例子：现有待切分字符串`ABCDEFGHIJ`，
    设词典中最大单词长度为`5`。那么按照算法首先取出`ABCDE`判断是否是单词， 如果是则切分到一个单词，否则舍弃最后一个字母接着判断，
    也就是判断`ABCD`是否是单词，依此类推，当只有一个字母时可以直接认定为是单词。 在成功切分出一个单词后对待切分字符串余下的部分
    再次执行上述过程。 *编写程序实现步骤`2`、`3` 描述的要求，并通过如下所示的主函数对进行验证，注意：除了指定添加的代码之外，不得修改
    `main` 函数其余部分。对  `main` 函数每修改一处，总分扣 `3` 分，最多扣    `10` 分。
    *本次考试考核
    `C` 语言程序设计，因此不可以使用`C + +`的` STL
    `的任何功能，如果需要添加下面样例之外的程序头文件，请举手得到监考老师批准。
    ** 程序： **
    '"""

    def read_file():
        with open('words.txt', encoding='utf-8') as f:
            words = f.read().split('\n')
        with open('input.txt', encoding='utf-8') as f:
            txt = f.read().split('\n')
        print(txt[0])
        print(txt[-1])
        i = -3
        if len(words) > 2:
            print(words[i])
            i += 1
        w = {}
        m = 0
        for word in words:
            le = len(word)
            if le > m:
                m = le
            w[word] = 1
        w['max_length'] = m
        return w, txt

    def txt_split(dictionary: dict, txt: str):
        width = dictionary.get('max_length')
        start = 0
        end = start + width
        length = len(txt)
        answer = []
        while start < length:
            if end > length:
                end = length
            if end == start + 1:
                answer.append(txt[start])
                start = end
                end = start + width
            s = txt[start:end]
            if dictionary.get(s):
                start = end
                end = start + width
                answer.append(s)
            else:
                end -= 1
        return ' '.join(answer)

    def write_to_file(txt):
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(txt)


def _by_2017():
    """
    ##### `2017`年保研上机题
    **要求：**
    文本文件`input.txt`里面放了一堆整数，仅仅以空格分隔，其中第一个整数为`k`，第二个整数代表维度，剩余的整数作为点的坐标.
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


def _2018(arr: list):
    """
    在20000个数中找一个满足下列条件的最大集合：
    集合中所有数之间的最大公因数是1（即两两互质）
    :param arr:
    :return:
    """
    # 准备工具
    arr = list(set(arr))
    arr.sort()
    size = len(arr)
    my_dict = {}

    # 因式分解
    def f1(n):
        if n < 4:
            return [n]
        i = 2
        factors = []
        while n > 1:
            f = 0
            while n % i == 0:
                f = 1
                n = n // i
            if f:
                factors.append(i)
            i += 1
        return factors

    def f2(old_set, new_set):
        i, j = 0, 0
        s1, s2 = len(old_set), len(new_set)
        while i < s1 and j < s2:
            if old_set[i] < new_set[j]:
                i += 1
            elif old_set[i] > new_set[j]:
                j += 1
            else:
                return False
        return True

    #求个数==各数因子
    for k in arr:
        my_dict[k] = f1(k)
    arr[0] = arr[0] if arr[0] != 1 else 2

    # 求最大子集
    M = 0
    ans = set()
    for i in range(size):
        p = set()
        vs = my_dict[arr[i]]
        p.add(arr[i])
        for j in range(size):
            this_factors =  my_dict[arr[j]]
            if f2(vs, this_factors):
                p.add(arr[j])
                vs = vs | this_factors
        if len(p) > M:
            M = len(p)
            ans = p

    return ans


def _2019():
    """
    (1)	编写函数read_file从文件中读取数据，将所有的整数按照其在文件中出现的顺序依次存储到数组arr中；
    (2)	编写函数print将数组arr显示在屏幕上，每行显示n个数，每个整数占6列；
    (3)	编写函数count统计数字0至9在数组arr所有整数中的出现次数，将结果放入数组res中（即res[0]存储数字0的出现次数，
    res[1]存储数字1的出现次数，其余以此类推）；
    (4)	编写函数print_res将数组res显示在屏幕上，每行显示5个数，可以复用步骤(2)中print函数；
    (5)	编写函数sort_array将数组arr中的整数按照因子和从小到大排序，如果两个整数的因子和相等，
    则按照它们的自然大小排序（注意：计算一个整数的因子和时包括1和其本身）；
    (6)	编写函数filter_array对数组arr中的整数进行筛选，结果继续保存在arr中，筛选规则如下：保留所有的偶数，
    同时保证这些偶数按照从小到大排序。说明：完成筛选之后，数组arr中的元素可以分成两部分，前半部分是有效内容，
    即所有的偶数，后半部分则是无效内容，参数size记录了数组arr中有效内容的长度（注意：筛选要求在原数组上进行，
    如使用新的辅助数组来完成筛选，扣10分）；
    (7)	编写函数write_file对数组arr中的有效内容（即所有偶数）进行质因数分解，并将结果输出到屏幕和文本文件output.txt中。
    输出要求：每一个整数的质因数分解结果占一行，具体显示格式如下图所示：
    :return:
    """

    def main():
        ls = read_file()
        res = count(ls)
        res_print(res)
        d = sort_array(ls)
        size = filter_arr(ls)
        write_file(ls, size, d)

    def read_file():
        with open('input.txt', encoding='utf-8') as file:
            arr = file.read().split()
        return list(map(int, arr))

    def arr_print(arr: list, n):
        length = len(arr)
        size = length // n
        for i in range(size):
            for j in range(i * n, (i + 1) * n):
                print('{:<6}'.format(arr[j]), end='')
            print()

    def count(arr: list):
        ls = [0] * 10
        for num in arr:
            if num == 0:
                ls[0] += 1
            else:
                while num:
                    num, h = divmod(num, 10)
                    ls[h] += 1
        return ls

    def res_print(res: list):
        arr_print(res, 5)

    def sort_array(ls: list):
        M = max(ls)
        primes = make_prime(M + 1)
        dic = {}

        def split(n):
            p = n
            i = n
            res = []
            while i:
                if primes[i] and n % i == 0:
                    n = n // i
                    res.append(i)
                else:
                    i -= 1
            res.sort()
            dic[p] = list(map(str, res))
            return sum(res)

        ls.sort()
        ls.sort(key=lambda x: split(x))
        return dic

    def filter_arr(arr: list):

        def sort(ls: list, start, end, fun):
            for i in range(start, end):
                f = 1
                for j in range(start, end - i - 1):
                    if fun(ls[j]) > fun(ls[j + 1]):
                        f = 0
                        ls[j], ls[j + 1] = ls[j + 1], ls[j]
                if f:
                    break

        sort(arr, 0, len(arr), fun=lambda x: x % 2)
        # arr.sort(key=lambda x:x%2)
        ou_end = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                ou_end = i
                break

        sort(arr, 0, ou_end + 1, lambda x: x)
        return ou_end + 1

    def write_file(arr: list, size, dic: dict):
        ans = []
        for item in arr[:size]:
            ls = '*'.join(dic.get(item))
            ans.append('{}={}'.format(item, ls))
        with open('Output.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(ans))

    main()

