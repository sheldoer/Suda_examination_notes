class Solution:
    def reverse(self, x: int) -> int:
        #利用数字转字符串再转数字的方法
        abs_x=int(str(abs(x))[::-1])
        if x > 0 and abs_x <= 2 ** 31 - 1:
            return abs_x
        if x < 0 and abs_x <= 2 ** 31:
            return -abs_x
        return 0
        '''#本人笨方法
        if x<10 and x>-10:
            return x
        flag=0
        if x<0:
            x=-x
            flag=-1
        y=0
        n=1
        while(x//(10**n)!=0):
            n+=1
        for i in range(n-1,-1,-1):
            y=y+x//(10**i)*10**(n-i-1)
            x=x%(10**i)
        if flag==-1:
            y=-y
        if y>2**31-1 or y<-2**31:
            return 0
        return y
        '''
p1=Solution()
print(p1.reverse(123))
