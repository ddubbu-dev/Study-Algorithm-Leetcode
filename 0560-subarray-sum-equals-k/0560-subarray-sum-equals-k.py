"""
[WARN] contiguous sequence
[HINT] sum(i,k) = sum(0,k) - sum(0,i) # sum of (i ~ k-1)

[참고자료]
https://leetcode.com/problems/subarray-sum-equals-k/solutions/3428039/easy-python-solution/

"""
class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        cnt = 0
        history = defaultdict(int) # 0으로 초기화

        for acc in accumulate(nums):
            diff = acc-target
            if diff in history: # diff = prev_acc 였다면?
                cnt += history[diff]
            if diff == 0:
                cnt += 1
            
            history[acc] += 1 # nums=[1, -1, 1, -1, 2] 처럼 누적합 반복일수도
        
        return cnt
