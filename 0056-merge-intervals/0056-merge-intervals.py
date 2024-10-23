INITIAL_END = -1

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []

        group_s = len(intervals)
        group_e = INITIAL_END
        for (s, e) in intervals:
            if s > group_e: # new!
                if group_e != INITIAL_END:
                    result.append([group_s, group_e])
                group_s = s
                group_e = e
            
            if s < group_s: # merge
                group_s = s
            if e > group_e:
                group_e = e
            
        
        result.append([group_s, group_e])

        return result
            

