class Solution:
    def isValid(self, sentence: str) -> bool:
        st = []

        try:
            for s in sentence:
                if s in ["(", "{", "["]:
                    st.append(s)
                elif s == ")":
                    poped = st.pop()
                    if poped != "(":
                        return False
                elif s == "}":
                    poped = st.pop()
                    if poped != "{":
                        return False  
                elif s == "]":
                    poped = st.pop()
                    if poped != "[":
                        return False
        except:
            return False
        
        if len(st):
            return False
        else:
            return True
