import numpy
class Solution:
    def rotate(self, matrix) -> None:
        """
        matrix: List[List[int]]
        Do not return anything, modify matrix in-place instead.
        """
       # Transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
		# Flip horizontally
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
            
        
            