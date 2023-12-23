class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        summa = sum(nums)
        leftsum = 0
        output = []
        for i in nums:
            output.append(abs(summa - leftsum - i))
            summa = summa - i
            leftsum = leftsum + i
        return output