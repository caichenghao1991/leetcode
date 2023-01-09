# 739. Daily Temperatures
from collections import deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        dq,res=deque(),[0]*len(temperatures)
        for i, v in enumerate(temperatures):
            while dq and temperatures[dq[-1]]<v:
                last=dq.pop()
                res[last]=i-last
            dq.append(i)
        return res
