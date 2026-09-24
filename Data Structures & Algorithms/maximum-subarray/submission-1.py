class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = sum(nums)
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            largest = max(curr, largest)
            curr = max(0, curr)
        return largest