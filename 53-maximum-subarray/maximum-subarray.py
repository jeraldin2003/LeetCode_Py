class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # summ = nums[0]
        # tempsum = 0      
        # for i in range(0, len(nums)):
        #     tempsum = 0
        #     for j in range(i,len(nums)):
        #         tempsum += nums[j]
        #         if(tempsum>summ):
        #             summ = tempsum

        #Using Kadan's Algorithm
        temp = 0
        main = nums[0]
        for num in nums:
            temp += num
            if(temp > main):
                main = temp
            if temp <= 0 :
                temp = 0
        return main
            
            


        return summ

