class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left <= right):
            if(nums[0] <= nums[len(nums)-1]):
                return nums[left]
            else:
                for i in range(len(nums)-1,-1,-1):
                    if nums[i]<nums[i-1]:
                        return nums[i]
