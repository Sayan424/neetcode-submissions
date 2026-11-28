from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        #returns hte key with the maximum count value
        return max(counts, key=counts.get)

