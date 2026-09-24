class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = sum(nums)
        curr = 0
        for i in range(len(nums)):
            curr = max(0, curr)
            curr += nums[i]
            largest = max(curr, largest)
        return largest