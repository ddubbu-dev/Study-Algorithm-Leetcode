class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        f_name = ""

        def do_fname():
            nonlocal f_name

            if not f_name:
                return

            if f_name == "..":
                if st:
                    st.pop() # "/"
                if st:
                    st.pop() # prev dir
            elif f_name != ".":
                st.append(f_name) # "." 제외한 "..." 까지는 f_name 취급
            f_name = "" # 초기화

        for s in path:
            if s == ".":
                f_name += s
            elif s == "/": # 끊기
                do_fname()
                if not st or (st and st[-1] != "/"):
                    st.append("/")
            else: # s is character
                f_name += s
        
        do_fname()

        
        if len(st) > 1 and st[-1] == '/':
            st.pop()
        if len(st) == 0:
            st.append("/")
        
        return "".join(st)


