class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        count = []
        for i in range(len(nums)):
            count.insert(index[i],nums[i])
        return count