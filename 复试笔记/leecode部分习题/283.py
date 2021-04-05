def move_list(nums:list):
    #调整数组顺序
    zero=nums.count(0)    #统计0的个数
    for i in range(zero): #先删去数组中的0
        nums.remove(0)
    nums.sort()
    for i in range(zero): #再在末尾添加相同个数的0
        nums.append(0)
    return nums
print(move_list([0,1,0,3,12]))
