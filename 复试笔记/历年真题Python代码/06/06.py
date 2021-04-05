
def make_prime(n):
    nums = [1] * n
    nums[0], nums[1] = 0, 0
    for i in range(2, n):
        if nums[i]:
            for j in range(i * i, n, i):
                nums[j] = 0
    return nums
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
_find_prime_excloud_9()
