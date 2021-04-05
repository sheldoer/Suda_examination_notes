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
