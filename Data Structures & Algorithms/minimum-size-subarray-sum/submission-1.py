class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("infinity")
        curr_sum = 0

        l = 0
        for r in range(0, len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                window = (r - l) + 1
                ans= min(window, ans)
                curr_sum -= nums[l]
                l += 1
        
        return 0 if ans == float("infinity") else ans