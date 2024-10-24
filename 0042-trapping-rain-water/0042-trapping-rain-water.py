"""
[참고] https://leetcode.com/problems/trapping-rain-water/solutions/4006957/100-solved-both-very-simple-way-and-optimized-way-to-solve-trapping-rain-water-problem/
"""

class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        stack = []
        water_trapped = 0
        current = 0
        
        while current < len(height):
            # 현재 기둥이 stack의 top보다 높은 경우 물이 고일 수 있음
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()  # 물이 고일 수 있는 지역의 바닥 기둥

                if not stack:
                    break  # 왼쪽 경계가 없으면 더 이상 물이 고일 수 없음
                
                distance = current - stack[-1] - 1  # 좌우 기둥 사이의 거리
                bounded_height = min(height[current], height[stack[-1]]) - height[top]  # 물이 고일 수 있는 높이

                water_trapped += distance * bounded_height
            
            stack.append(current)  # 현재 기둥 인덱스 stack에 추가
            current += 1
        
        return water_trapped
