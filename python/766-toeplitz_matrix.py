class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        v = matrix[0][0]
        for i in range(1, min(len(matrix), len(matrix[0]))):
            if v != matrix[i][i]:
                return False
        return True