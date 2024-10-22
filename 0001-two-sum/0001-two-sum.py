class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_table = {} # { complement_value : idx }
        for i in range(len(nums)):
            x = nums[i]
            y = target - x

            if y in complement_table:
                return [i, complement_table[y]]
            
            complement_table[x] = i