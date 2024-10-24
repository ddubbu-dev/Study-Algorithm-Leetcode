class Solution:
    def removeDuplicates(self, sentence: str) -> str:
        st = []

        for s in sentence:
            removed = False
            while st and st[-1] == s:
                st.pop()
                removed = True

            if not removed:
                st.append(s)
        

        return "".join(st)
