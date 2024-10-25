class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        prior = []
        for s in stones:
            heapq.heappush(prior, -s) # max-heap
        
        while len(prior) >= 2:
            s1 = -heapq.heappop(prior)
            s2 = -heapq.heappop(prior)

            heapq.heappush(prior, -abs(s1 - s2))

        return -prior[0]