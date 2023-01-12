# 108. Convert Sorted Array to Binary Search Tree
from typing import List, Optional
from tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            i = l + (r - l) // 2
            n = TreeNode(nums[i])
            n.left = helper(l, i - 1)
            n.right = helper(i + 1, r)
            return n
        return helper(0, len(nums) - 1)
