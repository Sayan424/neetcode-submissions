class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul=1
        for i in nums:
            mul *= i
        return 1 if mul > 0 else(-1 if mul < 0 else 0)