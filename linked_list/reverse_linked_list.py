# 206. Reverse Linked List
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy = None
        # pre, cur = dummy, head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     cur, pre = tmp, cur
        # return pre
        if not head or not head.next:
            return head
        x = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return x
