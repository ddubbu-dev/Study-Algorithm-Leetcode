class Solution:
    def minLength(self, sentence: str) -> int:
        st = []

        def validate():            
            while True:
                no_diff = True

                if len(st) >= 2:
                    sub = st[-2] + st[-1]
                    if sub == "AB" or sub == "CD":
                        st.pop()
                        st.pop()
                        no_diff = False

                if no_diff:
                    break                    
                

        for s in sentence:
            st.append(s)
            validate()
        
        return len(st)