class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sublistSums = []
        for sublist in accounts:
            sublistSum = sum(sublist)
            sublistSums.append(sublistSum)

        return max(sublistSums)