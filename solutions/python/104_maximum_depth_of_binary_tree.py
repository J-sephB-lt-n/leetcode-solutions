"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

NOTES:
    * Using list() or deque() gives the same runtime performance on leetcode
    * Using list() instead of deque() massively improves memory performance on leetcode
"""

from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = []  # deque()
        curr_node = root
        curr_depth = 1
        max_depth = 1
        while True:
            while curr_node:
                stack.append((curr_node, curr_depth))
                curr_node = curr_node.left
                if curr_node:
                    curr_depth += 1
                    if curr_depth > max_depth:
                        max_depth = curr_depth
            try:
                curr_node, curr_depth = stack.pop()
            except IndexError:
                break
            curr_node = curr_node.right
            if curr_node:
                curr_depth += 1
                if curr_depth > max_depth:
                    max_depth = curr_depth

        return max_depth
