# 134. Gas Station
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        cur, start=0,0
        for i in range(len(gas)):
            cur=cur+gas[i]-cost[i]
            if cur<0:
                cur=0
                start=i+1
        return start
