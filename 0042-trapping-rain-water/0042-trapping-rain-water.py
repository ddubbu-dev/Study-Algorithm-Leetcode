class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        stack = [] # (idx 모음) 역할: 왼쪽 경계 or 웅덩이
        water = 0
        idx = 0
        
        while idx < len(height):
            r_boundary = height[idx]

            while stack: # check 웅덩이
                base = height[stack[-1]] # 바닥
                if base >= r_boundary: # 웅덩이 X (오른쪽 경계 없음)
                    break
                
                base = height[stack.pop()]
                if not stack: # 웅덩이 X (왼쪽 경계 없음)
                    break
                
                l_boundary = height[stack[-1]]
                width = idx - stack[-1] - 1
                min_h = min(r_boundary, l_boundary) - base
                water += width * min_h
            
            stack.append(idx)
            idx += 1
        
        return water
