class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}
        ans = []

        for i in nums:
            hashy[i] = hashy.get(i, 0)+1

        buckets = [[] for _ in range(len(nums))]
        
        
        for num, count in hashy.items():
            buckets[count - 1].append(num)

        for i in range(len(buckets), 0, -1):
            for num in buckets[i-1]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        