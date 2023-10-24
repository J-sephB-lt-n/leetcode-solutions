"""
198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each 
house, return the maximum amount of money you can rob tonight without 
alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def rob_iterative(self, nums: list[int]) -> int:
        """this was the solution that I submitted"""
        if len(nums) < 3:
            return max(nums)
        self.memo[len(nums) - 1] = nums[-1]
        self.memo[len(nums) - 2] = max(nums[-2], nums[-1])
        for idx in range(len(nums) - 3, 0, -1):
            self.memo[idx] = max(nums[idx] + self.memo[idx + 2], self.memo[idx + 1])
        return max(nums[0] + self.memo[2], self.memo[1])

    def rob_recursive(self, nums: list[int]) -> int:
        """this is the solution which I wrote first, and it is unusably for len(nums) > 35"""
        if len(nums) > 2:
            return max(
                nums[0] + self.rob_recursive(nums[2:]),
                self.rob_recursive(nums[1:]),
            )
        else:
            return max(nums)


import random
import time

random_case = [random.randint(0, 9) for _ in range(35)]
print(random_case)
start_time = time.perf_counter()
print(Solution().rob_recursive(random_case))
print(f"rob_recursive: {time.perf_counter()-start_time:.2f} seconds")
start_time = time.perf_counter()
print(Solution().rob_iterative(random_case))
print(f"rob_iterative: {time.perf_counter()-start_time:.2f} seconds")
