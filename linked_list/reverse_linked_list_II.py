# 92. Reverse Linked List II      need rework
from linked_list import ListNode

successor = ListNode()


class Solution(object):
    def reverseFromStart(self, head, right):
        global successor
        if right == 1:
            successor = head.next
            return head
        tmp = self.reverseFromStart(head.next, right - 1)
        head.next.next = head
        head.next = successor
        return tmp

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseFromStart(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
