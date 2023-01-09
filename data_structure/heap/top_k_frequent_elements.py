# 347. Top K Frequent Elements
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq, pq = {}, []
        for n in nums:
            freq[n] = 1 if n not in freq else freq[n] + 1
        for val, freq in freq.items():
            heapq.heappush(pq, (freq, val))
            if len(pq) > k:
                heapq.heappop(pq)
        return [v[1] for v in pq]
