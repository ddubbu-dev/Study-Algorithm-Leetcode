class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for item in tokens:
            try:
                st.append(int(item))
            except: # not int
                tmp = 0
                op1 = st.pop()
                op2 = st.pop()
                if item == "+": tmp = op1 + op2
                elif item == "-": tmp = op2 - op1
                elif item == "*": tmp = op1 * op2
                elif item == "/": tmp = int(op2 / op1) # 단순 몫이 아님, 음수 주의

                # print(f"{op2}{item}{op1}={tmp}")
                st.append(tmp)

        return sum(st)