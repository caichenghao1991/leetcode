# 130. Surrounded Regions
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        h, w = len(board), len(board[0])

        def dfs(x, y):
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + i < h and 0 <= y + j < w and board[x + i][y + j] == 'O':
                    board[x + i][y + j] = 'V'
                    dfs(x + i, y + j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == h - 1 or j == 0 or j == w - 1) and board[i][j] == 'O':
                    board[i][j] = 'V'
                    dfs(i, j)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'

    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        h, w = len(board), len(board[0])
        q = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == h - 1 or j == 0 or j == w - 1) and board[i][j] == 'O':
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            board[x][y] = 'V'
            for m, n in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + m < h and 0 <= y + n < w and board[x + m][y + n] == 'O':
                    q.append((x + m, y + n))

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'