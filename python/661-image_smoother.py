from copy import deepcopy
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        img = deepcopy(M)
        m = len(M)
        n = len(M[0]) if m else 0
        for i in range(m):
            for j in range(n):
                neighbor = [M[x][y] for x in (i-1, i, i+1) for y in (j-1, j, j+1) if 0 <= x < m and 0 <= y < n]
                img[i][j] = sum(neighbor)//len(neighbor)
        return img