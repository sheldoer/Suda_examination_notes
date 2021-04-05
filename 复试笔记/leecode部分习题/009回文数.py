class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        for i in range(int(len(s)/2)):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
p1=Solution()
print(p1.isPalindrome(121))
