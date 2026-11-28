from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return list of tuples of top 1 most common the from the list 0th indexed tuple then 0th index in the tuple which contains the key
        return Counter(nums).most_common(1)[0][0]

