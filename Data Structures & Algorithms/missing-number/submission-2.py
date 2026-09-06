class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hashy = {-1:1}
        for i in nums:
            hashy[i] = 1

        ans = float("infinity")
        for i in nums:
            if i - 1 not in hashy:
                print(i)
                ans = min(ans, i - 1)
            if i + 1 not in hashy:
                ans = min(ans, i + 1)

        return ans