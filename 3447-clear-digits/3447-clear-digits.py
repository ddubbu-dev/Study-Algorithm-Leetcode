class Solution:
    def clearDigits(self, sentence: str) -> str:
        st = []

        for s in sentence:
            try: # type int
                num = int(s)
                st and st.pop()
            except:
                st.append(s)

        return "".join(st)
