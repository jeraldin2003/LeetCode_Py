class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if(nums[0] > target):
            for i in range(len(nums)-1,-1,-1):
                if(nums[i] == target):
                    return i
            return -1

        elif(nums[0] <= target):
            for i in range(0,len(nums)):
                if(nums[i] == target):
                    return i
            return -1