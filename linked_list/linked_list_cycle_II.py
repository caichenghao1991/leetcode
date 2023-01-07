# 142. Linked List Cycle II
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                new = head
                while fast and new:
                    if fast == new:
                        return fast
                    fast, new = fast.next, new.next
        return None
