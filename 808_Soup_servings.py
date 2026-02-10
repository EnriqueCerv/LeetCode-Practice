def soupServings(self, n: int) -> float:
        states = {}
        pa = 0
        pb = 0
        half = 0

        def backtrack(qa, qb):
            if qa <= 0 and qb <= 0:
                return 0.5
            elif qa <= 0:
                return 1
            elif qb <= 0:
                return 0

            if (qa, qb) in states:
                return states[(qa,qb)]

            prob = 0.25 * (
                backtrack(qa - 100, qb) +
                backtrack(qa - 75, qb - 25) +
                backtrack(qa - 50, qb - 50) +
                backtrack(qa - 25, qb - 75)
            )
            states[(qa, qb)] = prob
            return prob
        
        return 1 if n > 5000 else backtrack(n,n)

            
            