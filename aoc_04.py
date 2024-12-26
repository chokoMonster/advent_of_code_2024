import re
import pandas as pd
import numpy as np

def search_horizontal(grid, word):
    matches = 0
    for r in grid:
        matches += len(re.findall(word, ''.join(r)))
    return matches

def search_diagonal(grid, word):
    matches = 0
    for j in range(0, len(grid)-3):
        for i in range(0, len(grid[0])-3):
            if grid[i][j] == word[0]:
                if grid[i+1][j+1] == word[1]:
                    if grid[i+2][j+2] == word[2]:
                        if grid[i+3][j+3] == word[3]:
                            matches += 1
    return matches

def search_x(grid):
    matches = 0
    for j in range(1, len(grid)-1):
        for i in range(1, len(grid[0])-1):
            if grid[i][j] == 'A':
                if grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S':
                    if grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S':
                        matches += 1
    return matches


if __name__ == "__main__":
    word1 = 'XMAS'
    word2 = 'SAMX'

    f = open("input/04.txt", "r")
    lines = f.readlines()
    lines = [list(l.strip()) for l in lines]

    grid1 = pd.DataFrame(data=lines)
    grid2 = (grid1.transpose()).values
    grid1 = grid1.values
    grid3 = np.flip(grid1, 1)

    res = 0
    res += search_horizontal(grid1, word1)
    res += search_horizontal(grid1, word2)
    res += search_horizontal(grid2, word1)
    res += search_horizontal(grid2, word2)
    res += search_diagonal(grid1, word1)
    res += search_diagonal(grid1, word2)
    res += search_diagonal(grid3, word1)
    res += search_diagonal(grid3, word2)

    print(res)

    res2 = 0
    grid90 = np.rot90(grid1)
    grid180 = np.rot90(grid90)
    grid270 = np.rot90(grid180)
    res2 += search_x(grid1)
    res2 += search_x(grid90)
    res2 += search_x(grid180)
    res2 += search_x(grid270)

    print(res2)
