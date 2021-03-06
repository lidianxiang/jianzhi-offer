"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中
向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如
    [
    a b c e
    s f c s
    a d e e
    ]
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:
    """
    回溯法：
        首先遍历这个矩阵，找到与字符串str中第一个字符相同的矩阵元素ch。然后遍历ch的上下左右四个字符。如果有和字符串str中
        下个字符相同的，就把那个字符当作下一个字符（下一个遍历的起点），如果没有，就需要回退到上一个字符，然后重新遍历。为了
        避免路径重叠，需要一个辅助矩阵来记录路径的情况。
    """
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if matrix is None or rows < 1 or cols < 1 or path is None:
            return False
        visited = [0] * (rows * cols)

        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True
        hasPath = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[pathLength] and not \
                visited[row * cols + col]:
            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols,row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)
            if not hasPath:
                pathLength -= 1
                visited[row * cols + col] = False
        return hasPath
