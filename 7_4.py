## n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
## 입력 [1,4,3,2]
## 출력 4

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res=0
        for i in nums[::2]:
            res+=i
        return res
