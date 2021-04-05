
def make_prime(n):
    nums = [1] * n
    nums[0], nums[1] = 0, 0
    for i in range(2, n):
        if nums[i]:
            for j in range(i * i, n, i):
                nums[j] = 0
    return nums

def print_1000_9999():
    """
    `2011`年复试上机题
    **要求：**
    输出`1000-9999`中满足以下条件的所有数：
    * 该数是素数.
    * 十位数和个位数组成的数是素数，百位数和个位数组成的数是素数.
    * 个位数和百位数组成的数是素数，个位数和十位数组成的数是素数. 比如`1991`，
    个位和十位组成的数就是`19`.
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
print_1000_9999()
