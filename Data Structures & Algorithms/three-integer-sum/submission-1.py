class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        hashy = {}
        for i in range(len(nums)):
            if nums[i] in hashy:
                hashy[nums[i]] += 1
                continue
            hashy[nums[i]] = 1
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                su = (nums[i] + nums[j]) * -1
                
                if su in hashy:

                    hashy[su] -= 1
                    hashy[nums[j]] -= 1
                    hashy[nums[i]] -= 1
                    if hashy[nums[i]] >= 0 and hashy[nums[j]] >= 0 and hashy[su] >= 0:
                        an = sorted([nums[i], nums[j], su])
                        if an not in ans:
                            ans.append(an)
                    hashy[su] += 1
                    hashy[nums[j]] += 1
                    hashy[nums[i]] += 1
        return ans