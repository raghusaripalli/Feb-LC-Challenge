def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        
        csum = 0
        gsum = 0
        for i in range(1, l):
            csum += prices[i] - prices[i-1]
            if csum < 0:
                csum = 0
            gsum = max(gsum, csum)
            
        
        return gsum
