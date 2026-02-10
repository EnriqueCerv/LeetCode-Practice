def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x: x[1])
        y_min = min(y for _, y, _ in squares)
        y_max = max(y + l for _, y, l in squares)

        def area(y):
            below = above = 0
            for square in squares:
                yi, li = square[1], square[2]
                if yi + li < y:
                    below += li **2
                elif yi >= y:
                    above += li **2
                else:
                    y_bel = y - yi
                    y_ab = (yi + li) - y
                    below += y_bel * li
                    above += y_ab * li
            return below, above
        
        eps = 1e-5
        while y_max - y_min > eps:
            y_mid = (y_min + y_max) / 2
            below, above = area(y_mid)

            if below < above:
                y_min = y_mid
            else:
                y_max = y_mid

        return (y_min + y_max) / 2