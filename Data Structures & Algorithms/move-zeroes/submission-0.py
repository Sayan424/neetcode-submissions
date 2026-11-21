class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for x in nums:
            if x != 0:
                nums[pos] = x
                pos += 1 # when x = 1, pos = 1 & x = 2, pos = 2 and so on 
        for idx in range(pos, len(nums)): #pos = 3 
            nums[idx] = 0 #replaces all the remaining values with 0
        

