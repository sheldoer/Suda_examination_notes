class Solution:
    def maxArea(self, height) -> int:
        '''#本人超时代码
        num=0
        h=0
        for i in range(len(height)):
            for  j in range(len(height)-1,i-1,-1):
                th=min(height[i],height[j])
                if th>h:
                    tnum=(j-i)*th
                    if tnum>num:
                        num=tnum
                        h=th
        return num
    '''
        #双指针法
        i, j, res = 0, len(height) - 1, 0
            while i < j:
                if height[i] < height[j]:
                    res = max(res, height[i] * (j - i))
                    i += 1
                else:
                    res = max(res, height[j] * (j - i))
                    j -= 1
        return res
p1=Solution()
print(p1.maxArea([1,8,6,2,5,4,8,3,7]))
