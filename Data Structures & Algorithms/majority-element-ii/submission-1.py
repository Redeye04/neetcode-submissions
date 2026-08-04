class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        hashy = {}
        n = len(nums)
        for i in nums:
            if i not in hashy:
                hashy[i] = 1
            elif hashy[i] != -1:
                hashy[i] += 1
            
            if hashy[i] != -1 and hashy[i] > n // 3:
                hashy[i] = -1
                ans.append(i)
            
        return ans