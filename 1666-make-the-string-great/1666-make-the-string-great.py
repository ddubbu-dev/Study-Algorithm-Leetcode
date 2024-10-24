class Solution:
    def makeGood(self, sentence: str) -> str:
        st = []

        for s in sentence:
            added = False
            if st and (st[-1] != s) and (st[-1].upper() == s or st[-1] == s.upper()):
                st.pop()
                added = True

            if not added:
                st.append(s)
            # print(st)

        return "".join(st)
        
                 