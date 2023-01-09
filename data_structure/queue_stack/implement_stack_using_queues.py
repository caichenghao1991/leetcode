# 225. Implement Stack using Queues
from collections import deque


class MyStack(object):

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        x = self.q1.popleft() if self.q1 else None
        self.q1, self.q2 = self.q2, self.q1
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.q1[-1] if self.q1 else None

    def empty(self):
        """
        :rtype: bool
        """

        return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
