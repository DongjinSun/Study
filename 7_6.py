class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        i=0
        j=1
        res = 0
        while i<n-1:
            while i<n-1 and prices[i]>=prices[i+1]:
                i+=1
            j=i+1
            while j<n and prices[i]<prices[j]:
                res = max(res,prices[j]-prices[i])
            i=j
        return res
      
s = Solution()
print(s.maxProfit([1]))