class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max1 = 0
        max2 = 0
        sl = len(stones)
        while sl > 1:
            for i in range(sl):
                if stones[i] > max1:
                    max1 = stones[i]
            stones.remove(max1)
            sl -= 1

            for j in range(sl):
                if max2 < stones[j]:
                    max2 = stones[j]
            
            stones.remove(max2)

            dif = max(max1 - max2, max2 - max1)
            max1 = 0
            max2 = 0
            stones.append(dif)
        
        return stones[0]