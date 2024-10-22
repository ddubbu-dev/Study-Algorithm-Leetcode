"""
two pointer
- 정렬 필수!
- learning target: sum of group is 0
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        size = len(nums)
        for i in range(size-2):
            left = i + 1
            right = size - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else: # total == 0
                    tmp = (nums[i], nums[left], nums[right])
                    result.add(tmp)

                    left += 1
                    right -= 1

        return list(map(list, result))
        


