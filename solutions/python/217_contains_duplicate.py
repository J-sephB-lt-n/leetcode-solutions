# https://leetcode.com/problems/contains-duplicate


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup_dict = {}
        for num in nums:
            if num in lookup_dict:
                return True
            lookup_dict[num] = None
        return False
