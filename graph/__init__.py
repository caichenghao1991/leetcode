"""

    DFS, BFS, Dijkstra, A*, Topological sort

    Leetcode problems

    133. Clone Graph
    127. Word Ladder
    490. The Maze
    210. Course Scheduling
    269. Alien Dictionary

leetcode: 797. 133, 200, 2049
            207, 210.
            785.
            130, 323, 990.
            1135, 1584, 261.
            1135, 1584.
            1514, 1613, 743.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
