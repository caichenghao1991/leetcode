# 654. Maximum Binary Tree
from typing import List, Optional
from tree import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        m = max(nums)
        i = nums.index(m)
        node = TreeNode(m)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node
