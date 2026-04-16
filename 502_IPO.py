class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        import heapq
        n = len(profits)

        capital_min_heap = []
        for i in range(n):
            heapq.heappush(capital_min_heap, (capital[i], profits[i]))

        profit_max_heap = []
        for _ in range(k):
            while capital_min_heap and capital_min_heap[0][0] <= w:
                capital, profit = heapq.heappop(capital_min_heap)
                heapq.heappush_max(profit_max_heap, profit)
            
            w += heapq.heappop_max(profit_max_heap) if profit_max_heap else 0
        
        return w
