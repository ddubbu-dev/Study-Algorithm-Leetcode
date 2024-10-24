class Solution:
    def maxDepth(self, sentence: str) -> int:
        maxD = 0
        st = []

        for s in sentence:
            if s == "(":
                st.append(s)
            elif s == ")":
                maxD = max(len(st), maxD)
                st.pop()
            else:
                continue
        
        return maxD