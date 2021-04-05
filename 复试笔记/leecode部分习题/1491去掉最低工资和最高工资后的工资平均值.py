class Solution:
    def average(self, salary) -> float:
        salary.sort()
        return sum(salary[1:-1])/(len(salary)-2)
pl=Solution()
print(pl.average([4000,3000,1000,2000]))
