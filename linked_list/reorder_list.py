# 143. Reorder List
from linked_list import ListNode


class Solution(object):

    def reverse(self, head):
        if not head or not head.next: return head
        tmp = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return tmp

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        dummy = ListNode(next=head)
        fast, slow = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head2 = self.reverse(slow.next)

        slow.next = None

        cur = dummy
        while head and head2:
            tmp1, tmp2 = head.next, head2.next
            head2.next = tmp1
            head.next = head2
            head, head2 = tmp1, tmp2
            cur = cur.next.next
        if head:
            cur.next = head

        return dummy
