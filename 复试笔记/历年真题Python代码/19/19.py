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
