# 513. Find Bottom Left Tree Value
from collections import deque
from typing import Optional

from tree import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # res = 0
        # q = deque([root])
        # while q:
        #     s = len(q)
        #     for i in range(s):
        #         n = q.popleft()
        #         if i == 0:
        #             res = n.val
        #         if n.left:
        #             q.append(n.left)
        #         if n.right:
        #             q.append(n.right)
        # return res

        def traverse(root, depth):
            if not root:
                return 0, -1
            if root and not root.left and not root.right:
                return root.val, depth
            l = traverse(root.left, depth + 1)
            r = traverse(root.right, depth + 1)
            if r[1] > l[1]:
                return r[0], r[1]
            else:
                return l[0], l[1]

        return traverse(root, 1)[0]
