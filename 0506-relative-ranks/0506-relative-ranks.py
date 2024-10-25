class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        priority = []
        for i, score in enumerate(scores):
            heapq.heappush(priority, (-score, i)) # min-heap
        
        i = 0
        while priority:
            poped = heapq.heappop(priority)
            inner_i = poped[1]
            if i == 0:
                scores[inner_i] = "Gold Medal"
            elif i == 1:
                scores[inner_i] = "Silver Medal"
            elif i == 2:
                scores[inner_i] = "Bronze Medal"
            else:
                scores[inner_i] = str(i+1)

            i += 1

        return scores
        
        

        