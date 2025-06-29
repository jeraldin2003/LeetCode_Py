class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashbrown = defaultdict(int)
        for num in nums:
            hashbrown[num] += 1
            if hashbrown[num]>1:
                return True
        return False
