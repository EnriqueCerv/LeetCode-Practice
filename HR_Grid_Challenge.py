# %% Hacker rank grid challenge

def gridChallenge(grid):
    # Write your code here
    grid = [[char for char in st] for st in grid]
    print(grid)

    for i in range(len(grid)):
        index_array = [ord(ele) for ele in grid[i]]
        index_array.sort()
        grid[i] = [chr(ele) for ele in index_array]
    # for array in grid:
    #     index_array = [ord(ele) for ele in array]
    #     index_array.sort()
    #     array = [chr(ele) for ele in index_array]
    
    print(grid)
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    # grid = np.array(grid)
    # grid = grid.transpose()
    for array in grid:
        index_array = [ord(ele) for ele in array]
        isSorted = all(index_array[i] <= index_array[i + 1] for i in range(len(index_array) - 1))
        if not isSorted:
            return 'NO'
    return 'YES'

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

gridChallenge(grid)
