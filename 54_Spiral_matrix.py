def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        arr = []
        def spiral(row, col, direction_idx):
            if all(all(cell == '.' for cell in row) for row in matrix):
                return

            drow, dcol = directions[direction_idx]
            while True:
                arr.append(matrix[row][col])
                matrix[row][col] = '.'
                if row + drow < m and col + dcol < n and matrix[row + drow][col + dcol] != '.':
                    row += drow
                    col += dcol
                else:
                    break
            direction_idx = (direction_idx + 1) % 4
            drow, dcol = directions[direction_idx]
            spiral(row + drow, col + dcol, direction_idx)

        spiral(0,0,0)
        return arr
