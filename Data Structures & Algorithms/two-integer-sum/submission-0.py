class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        
        for i in range(len(nums)):
            if target - nums[i] in hashy:
                return [hashy[target - nums[i]], i]

            hashy[nums[i]] = i
        return
            