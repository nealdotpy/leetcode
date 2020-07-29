'''
62. Unique Paths - Medium
https://leetcode.com/problems/unique-paths/
'''
import math
import time

def time_this_function(function):
    def timed(*args, **kw):
        ts = time.time()
        result = function(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', function.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.8f ms' % \
                  (function.__name__, (te - ts) * 1000))
        return result
    return timed

class Solution:

    @time_this_function
    def nm_unique_paths(self, m, n):
        grid = [[1 for i in range(m)] for j in range(n)]
        # print(space_eff_grid)
        for j in range(1, m):
            for i in range(1, n):
                # print(i, j)
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        # print(grid)
        return grid[-1][-1]

    @time_this_function
    def two_m_unique_paths(self, m, n):
        space_eff_grid = [[1 for i in range(m)] for j in range(2)]
        for i in range(1, n):
            for j in range(1, m): # O(m)
                space_eff_grid[1][j] = space_eff_grid[0][j] + space_eff_grid[1][j-1]
            space_eff_grid[0] = space_eff_grid[1]
            space_eff_grid[1] = [1 for i in range(m)]

    @time_this_function
    def n_unique_paths(self, m: int, n: int) -> int:
        even_more_eff_grid = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                even_more_eff_grid[j] = even_more_eff_grid[j-1] + even_more_eff_grid[j]

        return even_more_eff_grid[-1]#space_eff_grid[0][-1]#grid[n-1][m-1]

    @time_this_function
    def eff_unique_paths(self, m, n):
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))



SOL = Solution()
print('there exist(s) {} path(s).'.format(SOL.nm_unique_paths(7, 3)))
print('there exist(s) {} path(s).'.format(SOL.two_m_unique_paths(7, 3)))
print('there exist(s) {} path(s).'.format(SOL.n_unique_paths(7, 3)))
print('there exist(s) {} path(s).'.format(SOL.eff_unique_paths(7, 3)))


print('there exist(s) {} path(s).'.format(SOL.nm_unique_paths(77, 93)))
print('there exist(s) {} path(s).'.format(SOL.two_m_unique_paths(77, 93)))
print('there exist(s) {} path(s).'.format(SOL.n_unique_paths(77, 93)))
print('there exist(s) {} path(s).'.format(SOL.eff_unique_paths(77, 93)))