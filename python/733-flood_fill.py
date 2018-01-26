class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, n, c = (len(image), len(image[0]), image[sr][sc])
        if c == newColor:
            return image
        image[sr][sc] = newColor
        li = [[sr, sc]]
        while len(li) != 0:
            x, y = li.pop()
            if x > 0 and image[x-1][y] == c:
                li.append([x-1, y])
                image[x-1][y] = newColor
            if x < m-1 and image[x+1][y] == c:
                li.append([x+1, y])
                image[x+1][y] = newColor
            if y > 0 and image[x][y-1] == c:
                li.append([x, y-1])
                image[x][y-1] = newColor
            if y < n-1 and image[x][y+1] == c:
                li.append([x, y+1])
                image[x][y+1] = newColor
        return image