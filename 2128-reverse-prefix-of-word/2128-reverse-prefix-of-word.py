class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        st = []

        occur = False
        for i in range(len(word)):
            s = word[i]
            st.append(s)

            if s == ch:
                occur = True
                break
        if not occur:
            return word
        return "".join(st[::-1]) + word[i+1:]

