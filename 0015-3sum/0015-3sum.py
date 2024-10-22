"""
two pointer
- 정렬 필수!
- learning target: sum of group is 0

중복값 처리
- tuple, set 이용하기
- 사전에 없애기
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        size = len(nums)
        for i in range(size-2):
            if i>0 and nums[i] == nums[i-1]: # 중복 제거
                continue

            left = i + 1
            right = size - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else: # total == 0
                    tmp = [nums[i], nums[left], nums[right]]
                    result.append(tmp)

                    left += 1
                    right -= 1

                    # 중복 제거 (각각해야, while 탈출 조건 부합)
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    
        return result
        


