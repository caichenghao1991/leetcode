# 160. Intersection of Two Linked Lists
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a and b:
            a, b = a.next, b.next
        pre, post = headA, headB
        if a:
            pre = headA
            while a:
                a, pre = a.next, pre.next
            post = headB
        if b:
            pre = headB
            while b:
                b, pre = b.next, pre.next
            post = headA
        while pre and post:
            if pre == post:
                return pre
            pre, post = pre.next, post.next
        return None
