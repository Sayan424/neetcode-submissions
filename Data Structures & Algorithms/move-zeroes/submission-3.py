class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indx = 0
        for i in nums:
            if i !=0 :
                nums[indx]=i
                indx+=1 

        for i in range(indx, len(nums)):
            nums[i] = 0
            indx += 1          


        
        

