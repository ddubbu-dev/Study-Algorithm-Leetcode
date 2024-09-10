class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def gen(result:str, left:int, right:int):
            if len(result) == 2*n:
                answer.append(result)
                return
            
            if left < n: 
                # left: 최대한 n까지 사용 가능
                gen(result + "(", left+1, right)
            if right < left:
                # right: left 열린만큼 사용 가능
                gen(result + ")", left, right+1)

        gen("", 0, 0)

        return answer