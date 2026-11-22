class Solution:
    def reverseBits(self, n: int) -> int:
        ny = format(n, "032b")
        return int(ny[::-1],2)