from random import randint


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
            this_factors = my_dict[arr[j]]
            if f2(vs, this_factors):
                p.add(arr[j])
                #vs = vs | this_factors
                vs=vs.union(this_factors)
        if len(p) > M:
            M = len(p)
            ans = p

    return ans


if __name__ == '__main__':
    arr = []
    for i in range(20000):
        arr.append(randint(0, 32768))
    print(_2018(arr))
