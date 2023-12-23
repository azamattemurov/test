class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = 0
        for counter, value in enumerate(nums):
            for x in nums[counter+1:]:
             if x == value:
                 n += 1
        return n