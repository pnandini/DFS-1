#Leetcode - 733
#Time - O(M*N)
#Space - O(1)

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        if color == newColor:
            return image
        else:
            self.dfs_helper(image, sr, sc, color, newColor)
        return image

    def dfs_helper(self, image, sr, sc, color, newColor):
        # base case
        if (sr < 0 or sr >= len(image) or sc >= len(image[0]) or sc < 0 or image[sr][sc] != color):
            return
        image[sr][sc] = newColor
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dir in dirs:
            i = dir[0] + sr  # get index
            j = dir[1] + sc  # get index
            # if (i >= 0 and i < len(image) and j < len(image[0]) and j <= 0):
            # if image[i][j] == color:
            # image[i][j] = newColor
            self.dfs_helper(image, i, j, color, newColor)

#BFS

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        # edge case
        # if not(image) or len(image) == 0:
        #    return image
        color = image[sr][sc]
        boolean_visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        if color == newColor:
            return image
        q = [(sr, sc)]
        boolean_visited[sr][sc] = True  # to check for visited arrays
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:

            # image[]
            curr = q.pop(0)
            # base case whenwe have to change color as it is in the queue
            image[curr[0]][curr[1]] = newColor
            boolean_visited[curr[0]][curr[1]] = True
            for dir in dirs:
                i = dir[0] + curr[0]  #
                j = dir[1] + curr[1]  #
                if (i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == color and not (
                boolean_visited[i][j])):
                    q.append((i, j))
        return image
#without visited array

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        # edge case
        # if not(image) or len(image) == 0:
        #    return image
        color = image[sr][sc]
        # boolean_visited = [[False for i in range(len(image[0]))] for j in range(len(image)) ]
        if color == newColor:
            return image
        q = [(sr, sc)]
        # boolean_visited[sr][sc] = True #to check for visited arrays
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:

            # image[]
            curr = q.pop(0)
            # base case whenwe have to change color as it is in the queue
            image[curr[0]][curr[1]] = newColor
            # boolean_visited[curr[0]][curr[1]] = True
            for dir in dirs:
                i = dir[0] + curr[0]  #
                j = dir[1] + curr[1]  #
                if (i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == color):
                    q.append((i, j))
        return image


###### Why was this not working??
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        if color == newColor:
            return image
        else:
            self.dfs_helper(image, sr, sc, color, newColor)
        return image

    def dfs_helper(self, image, sr, sc, color, newColor):
        # base case
        if (sr < 0 or sr > len(image) or sc > len(image[0]) or sc < 0):
            return

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dir in dirs:
            i = dir[0] + sr  # get index
            j = dir[1] + sc  # get index
            if (i >= 0 and i < len(image) and j < len(image[0]) and j <= 0):
                if image[i][j] == color:
                    image[i][j] = newColor
                    self.dfs_helper(image, i, j, color, newColor)