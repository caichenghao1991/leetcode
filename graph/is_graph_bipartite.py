# 785. Is Graph Bipartite?            need rework
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs_color(i):
            if not visited[i]:
                visited[i] = True
                color[i] = True
            for nb in graph[i]:
                if visited[nb]:
                    if color[nb] == color[i]:
                        return False
                else:
                    visited[nb] = True           # if not set visited, next recursion always set to True
                    color[nb] = not color[i]
                    if not dfs_color(nb):        # can't return dfs_color[i], otherwise miss branch
                        return False
            return True

        visited = [False] * len(graph)
        color = [False] * len(graph)
        for i in range(len(graph)):
            if not visited[i]:
                if not dfs_color(i):
                    return False
        return True

    def isBipartite2(self, graph: List[List[int]]) -> bool:
        color = [None] * len(graph)
        for i in range(len(graph)):
            if color[i] == None:
                color[i] = 1
                q = deque([i])
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if not color[nei]:
                            color[nei] = 1 - color[node]
                            q.append(nei)
                        else:
                            if color[node] == color[nei]:
                                return False
        return True
