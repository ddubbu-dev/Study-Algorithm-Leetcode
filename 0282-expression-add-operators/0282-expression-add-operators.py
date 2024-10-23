"""
[IDEA]
multiply 우선순위를 맞추기,
앞에서부터 진행하고, 곱 피연산자만큼 빼주기

https://leetcode.com/problems/expression-add-operators/
"""

class Solution:
    def addOperators(self, nums: str, target: int) -> List[str]:
        size = len(nums)
        result = []

        def dfs(start:int, acc_nums:int, prev:int, path:str):
            if start == size:
                if acc_nums == target:
                    result.append(path)
                return

            for end in range(start, size):
                if nums[start] == '0' and start != end: 
                    # Note: expressions should not contain leading zeros.
                    # 순수 0 가능
                    return

                cur = int(nums[start:end+1]) # = cur

                if start == 0:
                    dfs(end+1, cur, cur, str(cur)) # plus (only)
                else:
                    dfs(end+1, acc_nums + cur, cur, path+"+"+str(cur)) # plus
                    dfs(end+1, acc_nums - cur, -cur, path+"-"+str(cur)) # minus
                    dfs(end+1, acc_nums - prev + prev*cur, prev*cur, path+"*"+str(cur)) # multiply

        dfs(0,0,0,"")
        return result