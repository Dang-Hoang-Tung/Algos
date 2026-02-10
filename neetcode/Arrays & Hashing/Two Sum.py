class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_dict:
                return [my_dict[diff], i]
            if num not in my_dict:
                my_dict[num] = i
        return [-1, -1]
