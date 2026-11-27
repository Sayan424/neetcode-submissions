from collections import Counter 
class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s).values()
        max_odd = max(i for i in count  if i % 2 == 1)
        max_even = min(i for i in count if i % 2 == 0) # even needs to min to get the maximum difference
        return max_odd - max_even