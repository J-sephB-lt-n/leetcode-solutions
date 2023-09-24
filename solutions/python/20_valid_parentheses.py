"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        open_bracket_ref = {"(", "[", "{"}
        bracket_match_ref = {")": "(", "]": "[", "}": "{"}
        open_bracket_stack = deque()
        for char in s:
            if char in open_bracket_ref:
                open_bracket_stack.append(char)
            elif len(open_bracket_stack) == 0:
                return False
            elif bracket_match_ref[char] != open_bracket_stack.pop():
                return False
        if len(open_bracket_stack) > 0:
            return False
        return True


Solution().isValid(s="()[{()}]")
