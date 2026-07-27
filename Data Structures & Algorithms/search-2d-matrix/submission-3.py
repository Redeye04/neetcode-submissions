class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(nums, tar):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == tar:
                    return True
                elif nums[mid] > tar:
                    right = mid - 1
                elif nums[mid] < tar:
                    left = mid + 1
            
            return False

        # Find row that the target is in
        rows = 0
        cols = len(matrix[rows]) - 1

        while rows < len(matrix):
            print(matrix[rows][cols])
            if matrix[rows][cols] < target:
                rows += 1
            elif matrix[rows][cols] == target:
                return True
            else:
                break
        if rows > len(matrix) - 1:
            return False
            
        return binSearch(matrix[rows], target)
