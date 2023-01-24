from typing import Optional

from tree import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(root):
            if not root:
                return 0, 0
            if root in memo:
                return memo[root]
            l = dfs(root.left)
            r = dfs(root.right)
            memo[root] = max(l[0], l[1]) + max(r[0], r[1]), l[0] + r[0] + root.val
            return memo[root]

        dfs(root)
        return max(memo[root])
