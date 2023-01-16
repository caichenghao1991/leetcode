# 133. Clone Graph     need rework
from graph import Node


class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        d = {node: Node(node.val)}

        def dfs(n):
            for neigh in n.neighbors:
                if neigh not in d:
                    d[neigh] = Node(neigh.val)
                    dfs(neigh)
                d[neigh].neighbors.append(d[n])

        dfs(node)
        return d[node]

    # def cloneGraph(self, node):
    #     if not node: return
    #     d = {node: Node(node.val)}
    #     stack = [node]
    #     while stack:
    #         curNode = stack.pop()
    #         for nei in curNode.neighbors:
    #             if nei not in d:
    #                 d[nei] = Node(nei.val)
    #                 stack.append(nei)
    #             d[nei].neighbors.append(d[curNode])
    #     return d[node]
