class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fast(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            return fast(x * x, n//2) if n % 2 == 0 else x * fast(x, n - 1)
        
        return fast(x, abs(n)) if n >= 0 else 1/fast(x, abs(n))