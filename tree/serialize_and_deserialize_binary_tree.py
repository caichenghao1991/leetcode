# 297. Serialize and Deserialize Binary Tree     need rework
from collections import deque

from tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res, q = [], deque([])
        if root:
            q.append(root)
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(',')    # ['1', '2', '3', '#', '#', '4', '5', '#', '#', '#', '#']
        res = TreeNode(int(arr[0]))
        q, count = deque([res]), 1
        while q:
            node = q.popleft()
            if node:
                if arr[count] == '#':
                    l = None
                else:
                    l = TreeNode(int(arr[count]))
                    q.append(l)
                node.left = l
                count += 1

                if arr[count] == '#':
                    r = None
                else:
                    r = TreeNode(int(arr[count]))
                    q.append(r)
                node.right = r
                count += 1
        return res

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))