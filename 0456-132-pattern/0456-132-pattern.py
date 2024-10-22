"""
i < j < k (역참조)
n[i] < n[k] < n[j]

- stack 유형인 이유? 
- 과거값 토대로 n[k] 갱신
"""

import sys

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        n_k = -sys.maxsize
        for i in range(len(nums)-1, -1, -1):
            n_i = nums[i]
            if n_i < n_k: # n_j in 
                return True

            n_j = nums[i]
            # print("n_j", n_j)
            # print("stack", stack)
            while stack and stack[-1] < n_j:  # Q. 왜 while문 돌아야하지?
                n_k = max(stack[-1], n_k) # prev n_j -> n_k
                stack.pop()
            
            stack.append(n_j) # n_j보다 같거나 큰 값들만 존재
        
        return False