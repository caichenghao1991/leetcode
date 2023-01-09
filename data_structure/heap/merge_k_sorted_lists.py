# 23. Merge k Sorted Lists
import heapq

from linked_list import ListNode


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        curr = dummy
        pq = []
        for h in lists:
            if h:
                heapq.heappush(pq, (h.val, h))
        while pq:
            small = heapq.heappop(pq)
            curr.next = small[1]
            curr = curr.next
            next_small = small[1].next
            if next_small:
                heapq.heappush(pq, (next_small.val, next_small))
        return dummy.next
