# 24. Swap Nodes in Pairs
from linked_list import ListNode

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy = ListNode(next=head)
        # pre, cur = dummy, head
        # while cur and cur.next:
        #     temp = cur.next.next
        #     cur.next.next = cur
        #     pre.next = cur.next
        #     cur.next = temp
        #     pre, cur = cur, temp
        # return dummy.next
        if not head or not head.next: return head
        temp = self.swapPairs(head.next.next)
        n = head.next
        n.next = head
        head.next = temp
        return n
