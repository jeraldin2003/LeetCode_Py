class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(nums[0] <= nums[len(nums)-1]):
            return nums[0]
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]<nums[i-1]:
                    return nums[i]
