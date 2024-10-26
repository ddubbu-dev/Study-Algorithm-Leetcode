class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        visited = [False]*n

        def dfs(v: int):
            visited[v] = True
            
            for next_v in graph[v]:
                if next_v == destination:
                    return True
                if not visited[next_v]:
                    if dfs(next_v):
                        return True
                    else:
                        continue
            return False

        return dfs(source)