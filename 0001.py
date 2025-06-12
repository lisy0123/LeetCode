class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}

        for index, value in enumerate(nums):
            num = target - value
            if num in num_list:
                return [num_list[num], index]
            num_list[value] = index
            
        return []
