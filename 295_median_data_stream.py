class MedianFinder:

    def __init__(self):
        from bisect import insort
        self.vals = []
        self.len = 0

    def addNum(self, num: int) -> None:
        insort(self.vals, num)
        self.len += 1

    def findMedian(self) -> float:
        n = self.len
        is_odd = n % 2 != 0
        return self.vals[n//2] if is_odd else (self.vals[(n - 1) // 2] + self.vals[n // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        import heapq
        self.left = [] # max heap of smaller numbers
        self.right = [] # min heap of larger numbers

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right, heapq.heappushpop_max(self.left, num))

        if len(self.right) > len(self.left) + 1:
            heapq.heappush_max(self.left, heapq.heappop(self.right))

    def findMedian(self) -> float:
        is_even = len(self.left) == len(self.right)
        return (self.left[0] + self.right[0]) / 2 if is_even else self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()