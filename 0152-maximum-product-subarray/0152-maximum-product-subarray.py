class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        sufix = 1
        curmax = min(nums)
        for i in range(0,len(nums)):
            if(prefix == 0):
                prefix = 1
            if(sufix == 0):
                sufix = 1
            prefix *= nums[i]
            sufix *= nums[len(nums)-i-1]
            curmax = max(curmax , max(sufix,prefix))
        return curmax            