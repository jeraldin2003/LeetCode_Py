class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        sufix = [1]*len(nums)
        y = 1
        x = 1
        for i in range(0,len(nums)):
            prefix[i] = x
            x = nums[i]*x
        for i in range(len(nums)-1,-1,-1):
            sufix[i] = y
            y = nums[i]*y
        for i in range(0,len(nums)):
            nums[i] = prefix[i]*sufix[i]
        return nums
        
        
        