class Solution:
    def calculate(self, sentence: str) -> int:
        st = []
        pending_num = 0
        op = '+'

        for s in sentence + '+': # TODO: 
            try:
                num = int(s)
                pending_num = pending_num * 10 + num
            except: # not int
                if s == " ":
                    continue
                if op == "-":
                    st.append(-pending_num)
                elif op == "+":
                    st.append(pending_num)
                elif op == "*":
                    st.append(st.pop() * pending_num)
                elif op == "/":
                    poped = st.pop()
                    st.append(int(poped / pending_num))

                pending_num = 0
                op = s
        
        return sum(st)