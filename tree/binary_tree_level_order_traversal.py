# 102. Binary Tree Level Order Traversal
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, q = [], deque()
        if root: q.append(root)
        while q:
            l = len(q)
            lv = []
            for i in range(l):
                n = q.popleft()
                lv.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(lv)
        return res
