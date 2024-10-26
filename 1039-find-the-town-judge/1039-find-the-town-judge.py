"""
[a, b]: a trusts b (town judge)
- can identify judge
- dictionay key 값이 없어야, 나가는 방향이 없고
- (실패) 그러한 judge 후보들이 0/ 2개 이상이면, -1
- (성공) 그 아이

"""

class Solution:
    def findJudge_try(self, n: int, trust: List[List[int]]) -> int:
        S = set()
        for (s,e) in trust:
            S.add(e)

            if len(S) >= 2:
                return -1
        
        if len(S) == 1:
            return list(S)[0]
        else:
            return -1


    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        graph_reverse = defaultdict(list)
        for (s,e) in trust:
            graph[e].append(s) # 누가 e를 trust 하는지
            graph_reverse[s].append(e) #s가 누구를 trust
        
        candidates = []
        for e in range(1, n+1):
            if len(graph[e]) == n - 1:
                candidates.append(e) # 2번 조건
        
        for c in candidates: # 1번 조건
            if len(graph_reverse[c]) > 0:
                return -1

        if len(candidates) == 1:
            return candidates[0]
        else:
            return -1

        