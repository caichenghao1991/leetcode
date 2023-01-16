# 210. Course Schedule II
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        post, visited = [], [False] * numCourses
        current_path = [False] * numCourses
        self.cycle = False

        def dfs(curr):
            if current_path[curr]:
                self.cycle = True
                return
            if visited[curr]: return
            current_path[curr] = True
            visited[curr] = True
            for i in graph[curr]:
                dfs(i)
            current_path[curr] = False
            post.append(curr)

        for i in range(numCourses):
            dfs(i)
        return post[::-1] if not self.cycle else []