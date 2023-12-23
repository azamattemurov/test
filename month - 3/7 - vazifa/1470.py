class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        get_desired_index = lambda i: i * 2 if i<n else (i-n)*2+1
        for i in range(0,2*n):
            curr = i
            while nums[i]>=0:
                curr = get_desired_index(curr)
                nums[i], nums[curr]= nums[curr], -nums[i]
        for i in range(2*n):
            nums[i]= -nums[i]
        return nums