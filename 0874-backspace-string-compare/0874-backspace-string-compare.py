# stack - remove previous value
# (follow up) pointer - move each charcter

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []

        for i in range(len(s)):
            if s[i] == "#":
                st1 and st1.pop()
            else:
                st1.append(s[i])
            
        for i in range(len(t)):
            if t[i] == "#":
                st2 and st2.pop()
            else:
                st2.append(t[i])

        print(st1, st2)
        return "".join(st1) == "".join(st2)