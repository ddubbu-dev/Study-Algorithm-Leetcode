class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(s: int, e: int, player1: int, player2: int, trun_for_1: bool) -> bool:
            if s > e:
                return player1 >= player2  # winner
            if trun_for_1:  
                return dfs(s+1, e, player1 + nums[s], player2, not trun_for_1) \
                        or dfs(s, e-1, player1 + nums[e], player2, not trun_for_1)
            else:  
                return dfs(s+1, e, player1, player2 + nums[s], not trun_for_1) \
                        and dfs(s, e-1, player1, player2 + nums[e], not trun_for_1)
        
        return dfs(0, len(nums)-1, 0, 0, True)
