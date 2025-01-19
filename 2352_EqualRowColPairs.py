def equalPairs(grid):

        import numpy as np

        def equalPaircheck(grid):
            rows = set()
            for row in grid:
                st = ''
                for ele in row:
                    st += str(ele)
                rows.add(st)
            grid = np.array(grid)
            grid = grid.transpose()
            equal = 0

            for row in grid:
                st = ''
                for ele in row:
                    st += str(ele)
                if st in rows:
                    equal += 1
            return equal
        
        return max(equalPaircheck(grid), equalPaircheck(np.array(grid).transpose()))