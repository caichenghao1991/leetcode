# 19. Remove Nth Node From End of List
from linked_list import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        pre, post = dummy, head
        while n > 1:
            n -= 1
            post = post.next

        while post.next:
            pre, post = pre.next, post.next
        pre.next = pre.next.next
        return dummy.next
