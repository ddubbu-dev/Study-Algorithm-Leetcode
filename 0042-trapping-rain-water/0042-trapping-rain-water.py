"""
[참고] https://leetcode.com/problems/trapping-rain-water/solutions/4006957/100-solved-both-very-simple-way-and-optimized-way-to-solve-trapping-rain-water-problem/
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        
        l_max, r_max = 0, 0
        l, r = 0, len(height) - 1
        water = 0

        while l < r:
            if height[l] < height[r]: # 더 낮은 곳 물 웅덩이
                l_max = max(l_max, height[l])
                water += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                water += r_max - height[r]
                r -= 1
        
        return water