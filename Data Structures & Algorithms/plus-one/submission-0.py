class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=int("".join(str(i) for i in digits))+1
        n = str(n)
        digits = [int(i) for i in n]
        return digits