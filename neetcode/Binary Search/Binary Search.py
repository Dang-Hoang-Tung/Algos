class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def search_recursive(left_bound: int, right_bound: int) -> int:
            if right_bound <= left_bound:
                return -1

            mid: int = left_bound + ((right_bound - left_bound) // 2)
            
            if nums[mid] > target:
                return search_recursive(left_bound, mid)
            if nums[mid] < target:
                return search_recursive(mid+1, right_bound)
            
            return mid # nums[mid] == target

        return search_recursive(0, len(nums))
