"""
-- SOME NOTES --
here is how you can validate your work:
ref: https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
>>> from itertools import chain, combinations
>>> def powerset(iterable):
...    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
...    s = list(iterable)
...    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
>>> nums = [1, 2, 3, 4, 5]
>>> list( powerset(nums) )
...

# here is how you get all subsets of length 2:
>>> for i in range(0, len(nums)):
...    for j in range(i+1,len(nums)):
...        print(nums[i],nums[j])

# here is how you get all subsets of length 3:
>>> for i in range(0,len(nums)):
...    for j in range(i+1,len(nums)):
...        for k in range(j+1,len(nums)):
...            print(nums[i],nums[j],nums[k])
"""


class Solution:
    def get_all_subsets_of_length_n(self, n: int, nums: list[int]) -> list[int]:
        """Returns all subsets of length n"""
        subsets: list[list] = []
        idx_slots: list[int] = list(range(n))
        max_idx_ref: list[int] = [len(nums) - x - 1 for x in range(n)][::-1]
        curr_slot_idx: int = len(idx_slots) - 1
        subsets.append([nums[idx] for idx in idx_slots])
        while curr_slot_idx >= 0:
            if idx_slots[curr_slot_idx] < max_idx_ref[curr_slot_idx]:
                idx_slots[curr_slot_idx] += 1
                if curr_slot_idx < (n - 1):
                    counter = 1
                    for idx in range(curr_slot_idx + 1, n):
                        idx_slots[idx] = idx_slots[curr_slot_idx] + counter
                        counter += 1
                    curr_slot_idx: int = len(idx_slots) - 1
                subsets.append([nums[idx] for idx in idx_slots])
            else:
                curr_slot_idx -= 1
        return subsets

    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets: list[list[int]] = []
        for n in range(0, len(nums) + 1):
            subsets += self.get_all_subsets_of_length_n(n=n, nums=nums)
        return subsets


Solution().subsets(nums=[1, 2, 3, 4, 5])
