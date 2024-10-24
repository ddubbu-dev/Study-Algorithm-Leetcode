class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []

        for cmd in logs:
            if cmd == "../":
                st and st.pop()
            elif cmd == "./":
                continue
            else:
                st.append(cmd)
        
        return len(st)