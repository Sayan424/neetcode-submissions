from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist = 0
        count = Counter(arr) # creates an dictionary with count as values
        for key, value in count.items():
            if value == 1:
                dist += 1 
                if dist == k:
                    return key
        return ""