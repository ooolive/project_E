
# https://leetcode.com/problems/minimum-path-sum/

def foundation(grid, ta, x, y):
    #print(x, y)
    if x < len(grid)-1:
        sum_right = ta[x][y] + grid[x+1][y]
        org_right = ta[x+1][y]
        if org_right == -1:
            ta[x+1][y] = sum_right
            foundation(grid, ta, x+1, y)
        else:
            if org_right > sum_right:
                ta[x+1][y] = sum_right
                foundation(grid, ta, x+1, y)

    if y < len(grid[0])-1:
        sum_down = ta[x][y] + grid[x][y+1]
        org_down = ta[x][y+1]
        if org_down == -1:
            ta[x][y+1] = sum_down
            foundation(grid, ta, x, y+1)
        else:
            if org_down > sum_down:
                ta[x][y+1] = sum_down
                foundation(grid, ta, x, y+1)

class Solution_initial:
    def minPathSum(self, grid):
        ta = [[-1]*len(grid[0]) for i in xrange(len(grid))]
        ta[0][0] = grid[0][0]
        foundation(grid, ta, 0, 0)

        print(ta)

        return ta[-1][-1]

class Solution:
    def minPathSum(self, grid):
        lx, ly = len(grid), len(grid[0])
        ta = [[-1]*ly for i in xrange(lx)]

        ta[0][0] = grid[0][0]
        for i in xrange(1, lx):
            ta[i][0] = grid[i][0] + ta[i-1][0]
        for i in xrange(1, ly):
            ta[0][i] = grid[0][i] + ta[0][i-1]

        for i in xrange(1, lx):
            for j in xrange(1, ly):
                ta[i][j] = min(ta[i-1][j], ta[i][j-1]) + grid[i][j]
        return ta[-1][-1]

# tag DP，习惯性递归...
# 结果先是把坐标顺序搞错，然后 TLE...
# 这东西只需要输出 path 的 cost，直接迭代就行...
# 虽然代码有些啰嗦... 性能一般
# 话说有人直接用 grid 做临时空间...
# 还有人说他算法是 O(n) 的吓了老子一跳...
# 进去一看发现他把 N 定义成 mn loool

# 150316 PM

s = Solution()

t1 = [[1, 0, 5], [5, 6, 5], [7, 7, 8]]
print(s.minPathSum(t1))
print(s.minPathSum([[1, 2, 5], [3, 2, 1]]))
print(s.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))

