def read_file(url):
    #读取url文件
    with open(url,'r',encoding='utf-8')as fp:
        nums=fp.read().split()
    fp.close()
    return nums

def count_file(nums:list):
    #统计nums列表中的单词个数
    #print(nums)
    spe=['the','The','THe','THE']
    for i in nums:
        if i in spe:
            nums.remove(i)
    return list(set(nums))

def write_file(new:list):
    #写函数
    with open('new.txt','w')as fp:
        for i in new:
            fp.write(i.capitalize()+'\n')
    fp.close()
            

def main():
    #主函数，实现函数
    '''
    with open('org.dat','w')as fp:
        pass
    fp.close()
    '''
    nums=read_file('org.dat')
    new=count_file(nums)
    write_file(new)
    
if __name__=='__main__':
    main()

