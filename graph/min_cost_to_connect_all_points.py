# 1584. Min Cost to Connect All Points      need rework
import heapq
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, size):
        self.count = size
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)
        if r1 == r2:
            return
        self.parent[r2] = r1
        self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                graph.append((i, j, abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])))
        uf = UF(len(points))
        res, cnt = 0, 0
        for u, v, w in sorted(graph, key=lambda x: x[2]):
            if not uf.connected(u, v):
                res += w
                cnt += 1
                uf.union(u, v)
            if cnt >= len(points):
                break
        return res


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n, c = len(points), defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt + 1, ans + d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break
        return ans
