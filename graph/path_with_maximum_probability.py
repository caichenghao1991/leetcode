# 1514. Path with Maximum Probability
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([succProb[i], edges[i][1]])
            graph[edges[i][1]].append([succProb[i], edges[i][0]])

        distance = [0] * n
        distance[start] = 1
        pq = [(-1, start)]
        while pq:
            prob, cur = heapq.heappop(pq)
            if cur == end:
                return -prob
            if -prob < distance[cur]:
                continue

            for prob_nei, nei in graph[cur]:
                new_prob = distance[cur] * prob_nei

                if new_prob > distance[nei]:
                    distance[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))

        return distance[end]