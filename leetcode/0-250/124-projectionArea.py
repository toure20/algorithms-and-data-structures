def projectionArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    z = 0
    for col in grid:
        for row in col:
            if row != 0: z += 1
    
    x = 0
    for col in grid:
        maxx = 0
        for row in col:
            maxx = max(row, maxx)
        x += maxx

    y = 0    
    for i in range(len(grid)):
        maxy = 0
        for j in range(len(grid)):
            maxy = max(grid[j][i], maxy)
        y += maxy

    return z + x + y

def projectionArea2(grid):
    x, z = 0, 0
    for col in grid:
        x += max(col)
        for row in col:
            if row != 0: z += 1

    y = 0    
    for i in range(len(grid)):
        maxy = 0
        for j in range(len(grid)):
            maxy = max(grid[j][i], maxy)
        y += maxy

    return z + x + y

def projectionArea3(grid):
    N = len(grid)
    ans = 0

    for i in range(N):
        max_row, max_col = 0, 0
        for j in range(N):
            if grid[i][j]: ans += 1
            max_row = max(max_row, grid[i][j])
            max_col = max(max_col, grid[j][i])
        ans += max_row + max_col
        
    return ans

