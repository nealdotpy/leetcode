class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        istack = []
        num_islands, max_width, max_length = 0, len(grid[0]), len(grid)
        #istack.append((0, 0))
        for x in range(max_width): # O(x)
            for y in range(max_length): # O(y)
                if grid[y][x] != "1": continue
                if grid[y][x] == "1":
                    istack.append((y, x))   
                    grid[y][x] = "*"
                    num_islands += 1
                while istack: # O(istack)
                    i, j = istack.pop()
                    if i + 1 < max_length and grid[i+1][j] == "1":
                        grid[i+1][j] = "*"
                        istack.append((i+1, j))
                    if i - 1 >= 0 and grid[i-1][j] == "1":
                        grid[i-1][j] = "*"
                        istack.append((i-1, j))
                    if j + 1 < max_width and grid[i][j+1] == "1":
                        grid[i][j+1] = "*"
                        istack.append((i, j+1))
                    if j - 1 >= 0 and grid[i][j-1] == "1":
                        grid[i][j-1] = "*"
                        istack.append((i, j-1))
        return num_islands