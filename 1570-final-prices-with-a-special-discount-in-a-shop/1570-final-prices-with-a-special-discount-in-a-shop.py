# Why Stack ?

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        size = len(prices)
        result = []

        for i in range(size):
            for j in range(i+1, size):
                if prices[i] >= prices[j]:
                    result.append(prices[i] - prices[j])
                    break
            
            if i == len(result): # can't append
                result.append(prices[i])

        return result