"""
[문제 이해]
0(circular) 선호됨 > 1(square)
"""
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        sand_q = deque(sandwiches)

        loop = 0
        while q:
            if len(q) == loop: # can't eat
                break

            poped = q.popleft()
            if poped == sand_q[0]:
                sand_q.popleft()
                loop = 0
            else:
                q.append(poped)
                loop += 1
                

        return len(q)
        