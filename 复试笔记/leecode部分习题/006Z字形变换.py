class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        s2=''
        i=0
        for h in range(0,numRows):
            j=h
            while j<len(s):
                s2=s2+s[j]
                if h!=0 and h!=numRows-1:
                    k=j+numRows*2-2-2*h
                    if k<len(s):
                        s2=s2+s[k]
                j=j+numRows*2-2
        
        return s2
p1=Solution()
print(p1.convert("paypalishiring",3))
