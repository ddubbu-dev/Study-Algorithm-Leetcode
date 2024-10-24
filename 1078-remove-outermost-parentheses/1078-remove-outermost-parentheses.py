# outermost : open/close 개수 같을 때

class Solution:
    def removeOuterParentheses(self, sentence: str) -> str:
        st = []
        nopen = 0
        nclose = 0

        for s in sentence:
            if s == "(":
                if nopen == nclose:
                    nopen += 1
                    continue
                st.append(s)
                nopen += 1
            else:
                nclose += 1
                if nopen == nclose:
                    continue
                else:
                    st.append(s)

        return "".join(st)