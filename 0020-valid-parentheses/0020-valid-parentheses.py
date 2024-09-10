class Solution:
    def isValid(self, word: str) -> bool:
        
        stack = []
        for s in word:
            if s == "(" or s == "{" or s == "[":
                stack.append(s)
                continue
            
            if not stack:
                return False

            poped = stack.pop()

            if (poped == "(" and s == ")") or (poped == "{" and s == "}") or (poped == "[" and s == "]"):
                continue    
            
            return False


        if len(stack) > 0:
            return False

        return True