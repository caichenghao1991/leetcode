# 707. Design Linked List
class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.dummy = Node(None)
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.size or index < 0: return -1
        cur = self.dummy.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new = Node(val, self.dummy.next)
        self.dummy.next = new
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = Node(val, None)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.size >= index >= 0:
            cur = self.dummy
            while index > 0:
                cur = cur.next
                index -= 1
            new = Node(val, cur.next)
            cur.next = new
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < self.size and index >= 0:
            cur = self.dummy
            while index > 0:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)