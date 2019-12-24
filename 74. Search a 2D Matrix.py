class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # matrix: List[List[int]]
        for x in matrix:
            if len(x) == 0:
                return False
            if target in x:
                return True
            elif target < x[-1]:
                return False
                
        return False