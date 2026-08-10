class Solution:
    def findMin(self, nums: List[int]) -> int:
        cmp1 = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                cmp1 = min(cmp1, nums[left])
                break
                
            mid = (left + right) // 2
            cmp1 = min(cmp1, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return cmp1