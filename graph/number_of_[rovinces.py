# 547. Number of Provinces
class UF:
    def __init__(self,size):
        self.count=size
        self.parent=[i for i in range(size)]
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        r1 =self.find(x)
        r2=self.find(y)
        if r1 == r2:
            return
        self.parent[r2]=r1
        self.count -=1
    def connected(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf=UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i!=j and isConnected[i][j]==1:
                    print(i,j)
                    uf.union(i,j)
        return uf.count
