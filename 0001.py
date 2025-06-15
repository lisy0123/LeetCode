class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for key, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], key]
            nums_map[num] = key
