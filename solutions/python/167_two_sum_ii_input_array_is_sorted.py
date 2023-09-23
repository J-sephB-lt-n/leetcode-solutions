class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx = 0
        right_idx = 1
        max_right_idx = len(numbers) - 1
        last_x_num_checked = None
        while True:
            if numbers[left_idx] == last_x_num_checked:
                left_idx += 1
            else:
                last_x_num_checked = numbers[left_idx]
                right_idx = left_idx + 1
                required_value = target - numbers[left_idx]
                while numbers[right_idx] <= required_value:
                    if numbers[right_idx] == required_value:
                        return [left_idx + 1, right_idx + 1]
                    if right_idx < max_right_idx:
                        right_idx += 1
                    else:
                        break
                left_idx += 1


Solution().twoSum(numbers=[-3, -2, -2, -2, -2, -2, 1, 1, 2], target=2)
