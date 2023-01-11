# 501. Find Mode in Binary Search Tree
from typing import Optional, List
from tree import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        travel = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            travel.append(root.val)
            traverse(root.right)

        traverse(root)

        res, counter = [travel[0]], 1
        cur_max = 1
        for i in range(1, len(travel)):
            if travel[i] == travel[i - 1]:
                counter += 1
            else:
                counter = 1
            if counter == cur_max:
                res.append(travel[i])
            elif counter > cur_max:
                cur_max = counter
                res = [travel[i]]
        return res

