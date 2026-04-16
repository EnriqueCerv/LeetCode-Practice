class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])

        for row in matrix:
            left, right = 0, n - 1

            while left <= right:
                mid = (right + left) // 2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    left = mid + 1
                else: 
                    right = mid - 1
        
        return False
                
