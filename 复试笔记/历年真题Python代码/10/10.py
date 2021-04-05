def _count_n():
    """
     `2010`年复试上机题
    **要求：**
    * 从`FTP`上下载`make.exe`和`org.dat`，运行`make.exe`输入准考证后三位生成`data.txt`
      ，文件为二进制编码.
    * `data.txt`内存有`2048`个整数，其中前`n`个为非`0`数，后`2048-n`个数为`0`，
      将其读入数组，计算非零数的个数`n`.
    * 选出`n`个数中的最大数和最小数.
    * 选出`n`个数中最大素数.
    * 将`n`个数从大到小排序，并平均分成三段(若`n`非`3`的整数倍，则不考虑最后的`1-2`个数)，
      选出中间段的最大数和最小数.
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
