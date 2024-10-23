class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*n

        result = []
        for course, pre in prerequisites:
            graph[pre].append(course) # pre->course
            indegree[course] += 1   
 
        q = deque() # 위상정렬 템플릿, degree=0 시작점으로부터
        for i in range(n): # 나홀로 수강과목까지 챙김
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            result.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return len(result) == n # 순환구조가 발생했는지