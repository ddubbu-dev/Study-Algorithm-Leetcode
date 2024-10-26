class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        
        mark = [] # record bool which is even?
        ans = []
        
        arr = map(int, str(num))
        for n in arr:
            if n%2:
                even.append(-n)
                mark.append(True)
            else:
                odd.append(-n)
                mark.append(False)
        
        heapq.heapify(odd)
        heapq.heapify(even)


        for i in range(len(mark)):
            base = even if mark[i] else odd
            ans.append(str(-heapq.heappop(base)))
        
        return int("".join(ans))

