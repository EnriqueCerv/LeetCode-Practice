def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        sieve = [i if i % 2 == 1 else 0 for i in range(2, n)]
        sieve[0] = 2

        for i, ele in enumerate(sieve):
            if ele == 0:
                continue
            
            cur_idx = i + ele

            while cur_idx < n-2:
                sieve[cur_idx] = 0
                cur_idx += ele
        
        return len([ele for ele in sieve if ele != 0])