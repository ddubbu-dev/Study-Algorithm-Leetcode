class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0
        places = []  # 각 (0~n-1) column별로 Queen이 놓인 row

        def validate(row)->bool:
            if row in places: # 가로
                return False
            
            col = len(places)
            for j in range(len(places)):
                i = places[j]
                if i-j == row-col or i+j == row+col: # 대각선 정방향/역방향
                    return False
            return True
        
        
        def dfs(col):
            nonlocal cnt 
            if len(places) == n:
                cnt +=1
                return
            
            for row in range(n):
                if(validate(row)):
                    places.append(row)
                    dfs(col+1)
                    places.pop()
        
        dfs(0)

        return cnt



