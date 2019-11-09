class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # edge case
        if not (matrix) and len(matrix) == 0:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                if matrix[i][j] != 0:
                    matrix[i][j] = self.dfs_helper(matrix, i, j)
        return matrix

    def dfs_helper(self, matrix, i, j):  # index of cell
        # edge case
        # if matrix[i][j]
        q = []
        q.append((i, j))
        dist = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            size = len(q)
            for i in range(0, size, 1):
                # if curr[0]:
                curr = q.pop(0)
                for dir in dirs:

                    r = curr[0] + dir[0]
                    c = curr[1] + dir[1]

                    if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]):
                        if matrix[r][c] == 0:
                            return dist + 1
                        else:
                            q.append((r, c))
            dist += 1