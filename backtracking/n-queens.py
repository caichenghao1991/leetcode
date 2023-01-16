# 51. N-Queens
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: return []
        res = []
        board = [['.'] * n for _ in range(n)]

        def valid(board, x, y):
            size = len(board)
            for i in range(size):
                if board[i][y] == 'Q':
                    return False
            for i in range(1, size):
                if x - i >= 0 and y - i >= 0:
                    if board[x - i][y - i] == 'Q':
                        return False

            for i in range(1, size):
                if x - i >= 0 and y + i < size:
                    if board[x - i][y + i] == 'Q':
                        return False

            return True

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for i in range(n):
                if not valid(board, row, i):
                    continue
                board[row][i] = 'Q'
                backtrack(row + 1)
                board[row][i] = '.'

        backtrack(0)
        return res
