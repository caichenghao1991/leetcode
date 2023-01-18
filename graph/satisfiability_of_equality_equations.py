# 990. Satisfiability of Equality Equations
from collections import defaultdict
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        count = 0
        same = defaultdict(list)
        diff = defaultdict(list)
        values = {}
        for eq in equations:
            if eq[1] == '=':
                same[eq[0]].append(eq[3])
                same[eq[3]].append(eq[0])
            else:
                diff[eq[0]].append(eq[3])
                diff[eq[3]].append(eq[0])

        for v in diff:
            if v in diff[v]:
                return False

        def dfs(curr):
            for nei in same[curr]:
                if nei not in values:
                    values[nei] = values[curr]
                    dfs(nei)

        for v in same.keys():
            if v not in values:
                values[v] = count
                dfs(v)
                count += 1
        for v in diff.keys():
            val = values.get(v, None)
            if val != None:
                for v2 in diff[v]:
                    val2 = values.get(v2, None)
                    if val2 != None and val2 == val:
                        return False


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.count = size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        self.root[rootY] = rootX
        self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution2:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        equations_same = [x for x in equations if x[1] == '=']
        equations_notsame = [x for x in equations if x[1] == '!']

        for eq in equations_same:
            xi, yi = ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a')
            uf.union(xi, yi)

        for eq in equations_notsame:
            xi, yi = ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a')
            if uf.connected(xi, yi):
                return False
        return True
