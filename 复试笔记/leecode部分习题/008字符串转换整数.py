import re
class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        #re简洁方法
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
        '''#本人方法
        s=s.strip()
        flag=True
        if len(s)==0:
            return 0
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                flag=False
            s=s[1:]    
        n=0
        for i in s:
            if i<='9' and i>='0':
                 n+=1
            else:
                break 
        num=0 if n==0 else int(s[0:n])
        if flag==True:
            return min(2**31-1,num)
        return max(-2**31,-num)
        
p1=Solution()
print(p1.myAtoi("+-+21k"))
                
        
