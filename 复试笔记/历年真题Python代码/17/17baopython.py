def read_file(url):
    #读文件
    with open(url, 'r')as fp:
        nums = list(map(int, fp.read().split()))    #将所有数字转化为整数形式，存储到nums数组里
    return nums


def find_distance(nums):
    #计算点距离
    k = nums[0]         #先将k值存储
    dimen = nums[1]     #存储维度
    nums = nums[2:]     #截取点数据
    f = lambda
