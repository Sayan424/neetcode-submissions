class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        maxi = 0
        for i in nums:
            if i == 0:
                k=0
            else:
                k+=1
                if k > maxi:
                    maxi = k
        return maxi