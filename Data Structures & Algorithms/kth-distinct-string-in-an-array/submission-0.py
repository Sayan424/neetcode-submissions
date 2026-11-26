from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr) # creates an dictionary with count as values
        for i in arr:
            if count[i] == 1:
                k-=1 #k at "a" becomes 0 and triggers next line
                if k == 0:
                    return i
        return ""