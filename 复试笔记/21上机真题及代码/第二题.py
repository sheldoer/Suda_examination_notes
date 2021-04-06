'''
第二题题目:给定指定整数，找到从1到该数的二进制表示中所有1的数目大于0的数字，
存到返回数组中
例如：15二进制表示为‘0b1111’,
其中[1, 3, 5, 6, 7, 11, 13, 14, 15]二进制表示1的数目大于0的数目
'''
def find_number(n):
    res=[]
    for i in range(n+1):
        s=bin(i)[2:]                #remove '0b'
        if s.count('1')>s.count('0'):
            res.append(i)
    return res
if __name__=='__main__':
    print(find_number(15))
        
