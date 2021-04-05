class Solution:
    #在未排序的数组中找到第 k 个最大的元素。
    #请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[-k]
pl=Solution()
print(pl.findKthLargest([3,2,3,1,2,4,5,5,6],4))
