## 417. Pacific Atlantic Water Flow

[leetcode link](https://leetcode.com/problems/pacific-atlantic-water-flow/)

### Notes

i got the solution from neetcode as i can't do it well in the first try, [YouTube Video](https://www.youtube.com/watch?v=s-VkcjHqkGI)

the idea is to do a "modified" DFS, where the next valid position is not only the next position in bounds, but also that the current "height" is smaller or equal to the next one proposed

then we need to run that DFS from top and from bottom of the grid

also we need to run that DFS from the most-left and most-right columns of the grid

i think i will revisit this exercise and do it again

### Source code (watch it only if we can't find a solution)

<details>
    <summary>Solution </summary>

```python
tests = [
    [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ],
]

class Solution:
    def dfs(self, grid: list[list[int]], i: int, j: int, visited: set, previous_height: int) -> None:
        n = len(grid)
        m = len(grid[0])

        if 0 <= i < n and \
            0 <= j < m and \
            previous_height <= grid[i][j] and \
            (i, j) not in visited:

            visited.add((i, j))

            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                self.dfs(grid, ni, nj, visited, grid[i][j])

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n = len(heights)
        m = len(heights[0])

        visited_pac = set()
        visited_atl = set()

        for j in range(0, m):
            self.dfs(heights, 0, j, visited_pac, heights[0][j])
            self.dfs(heights, n-1, j, visited_atl, heights[n-1][j])

        for i in range(0, n):
            self.dfs(heights, i, 0, visited_pac, heights[i][0])
            self.dfs(heights, i, m-1, visited_atl, heights[i][m-1])

        out = []

        for i in range(0, n):
            for j in range(0, m):
                if (i, j) in visited_pac and (i, j) in visited_atl:
                    out.append([i, j])

        return out

for test in tests:
    out = Solution().pacificAtlantic(test)
    print('out, ', out)
```

</details> 
