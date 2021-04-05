def judge_seq(res: list):
    #判断是否有等差为1的数列
    new = sorted(set(res))     #生成没有重复且有顺序的new序列
    i = 0
    #print(new)
    length = len(new)
    while i < length:
        for j in range(1, 5):
            if i+j >= len(new) or new[i+j]-new[i+j-1] != 1: #如果5个以内不等差，则直接截断
                i = i+j
                break
            if j == 4:
                return i, new
    return -1, new


def main():
    res = list(map(int, (input('请输入一系列数字').split())))
    s, new = judge_seq(res)
    #print(s, new)
    if s == -1:
        print("查找失败，列表里不含有等差为1的数列")
    else:
        print("存在等差数列，分别是：")
        for i in range(5):
            print(new[s+i])


if __name__ == '__main__':
    while True:
        main()
