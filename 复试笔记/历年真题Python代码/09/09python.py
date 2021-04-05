import re
def read_file():
    #读取文件内容
    with open('org.dat','r')as fp:
        nums=fp.read().split(',')
    fp.close()
    return nums

def ten_num(nums:list):
    for i in range(len(nums)):
        nums[i]=nums[i].replace(' ','')
        if nums[i][0]=='0':
            nums[i]='0o'+nums[i][1:]
    num=list(map(eval,nums))
    return num
    '''
        if re.search('\s*0\s*[0-9]*\s*',nums[i]):
            nums[i]=eight_to_ten(i)
    '''    

def write_file(num:list):
    num=map(str,num)
    with open('new.txt','w')as fp:
        fp.write('\n'.join(num))
        '''
        for i in num:
            fp.write(str(i)+'\n')
            '''
    fp.close()

def main():
    '''
    with open('org.dat','w')as fp:
        pass
    fp.close()
    '''
    nums=read_file()
    
    num=ten_num(nums)
    write_file(num)

if __name__=='__main__':
    main()
