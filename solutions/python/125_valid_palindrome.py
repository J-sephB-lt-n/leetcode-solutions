import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_alphanum = re.compile("[\W_]+").sub("", s).lower()
        if len(s_alphanum) == 0:
            return True
        # print(s_alphanum)
        left_idx = 0
        right_idx = len(s_alphanum) - 1
        s_alphanum[right_idx]
        while right_idx > left_idx:
            # print(s_alphanum[left_idx], s_alphanum[right_idx])
            if s_alphanum[left_idx] != s_alphanum[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True


Solution().isPalindrome("Satan-Oscillate-My-Metallic-Sonatas")
