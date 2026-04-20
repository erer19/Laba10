# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return None

        cur = root
        prev = None
        while cur and cur.val != key:
            prev = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if cur is None:
            return root

        def replace_node(prev, cur, new_child):
            if prev is None:
                return new_child
            if prev.left == cur:
                prev.left = new_child
            else:
                prev.right = new_child
            return root

        if cur.left is None:
            return replace_node(prev, cur, cur.right)
        if cur.right is None:
            return replace_node(prev, cur, cur.left)

        prev_node = cur
        node = cur.right
        while node.left is not None:
            prev_node = node
            node = node.left
        cur.val = node.val
        if prev_node.left == node:
            prev_node.left = node.right
        else:
            prev_node.right = node.right
        return root
