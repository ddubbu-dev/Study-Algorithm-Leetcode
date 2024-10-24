"""
Q. Stack 유형인 이유
A. prev 값을 토대로 D/C operate
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            print(op)

            if op == "C":
                st.pop()
            elif op == "D":
                st.append(st[-1]*2)
            elif op == "+":
                st.append(st[-1] + st[-2])
            else:
                st.append(int(op))


        return sum(st)
