"""
[방법]
- 모든 edge 간의 연결 길이 체크
- (v) 모든 edge에 존재하는 vertex 
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        center_candidate1 = 0
        center_candidate2 = 0
        for u,v in edges:
            if u == center_candidate1 or u == center_candidate2:
                return u
            if v == center_candidate1 or v == center_candidate2:
                return v

            center_candidate1 = u
            center_candidate2 = v
