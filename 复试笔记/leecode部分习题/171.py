def _171(s):
    nums=0
    for i in range(1,len(s)+1):
        num=ord(s[-i])-ord('A')+1
        nums+=num*(26**(i-1))
    return nums
if __name__=='__main__':
    s="A"
    print(_171(s))
