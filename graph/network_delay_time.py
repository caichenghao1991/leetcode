# 743. Network Delay Time   need rework
import heapq
from collections import deque, defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for frm, to, cost in times:
            graph[frm].append([cost, to])
        distance = [10001] * (n + 1)
        distance[k], distance[0] = 0, 0
        pq = [(0, k)]

        while pq:
            w, j = heapq.heappop(pq)
            if w > distance[j]:
                continue
            # if j in graph:
            for w2, nei in graph[j]:
                d = w2 + distance[j]
                if d < distance[nei]:
                    distance[nei] = d
                    heapq.heappush(pq, (d, nei))
        res = 0
        for d in distance:
            if d == 10001:
                return -1
            res = max(res, d)
        return res