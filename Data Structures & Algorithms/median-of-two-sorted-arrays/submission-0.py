class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)

        n = len(nums)
        if n % 2 != 0:
            return float(nums[n//2])
        else:
            print(nums)
            ans = nums[n//2] + nums[(n//2) - 1]
            return ans / 2
        