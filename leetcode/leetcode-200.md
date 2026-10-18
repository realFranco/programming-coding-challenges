## 200. Number of Islands

[leetcode link]https://leetcode.com/problems/number-of-islands/description/)

### Notes

since the moment i read the problem and check the input data i notice that the solution could be driven by using a BFS inside the Matrix (grid-bfs).

remember that the BFS implementation "may" use a queue inside the `while` loop to store the new valid solutions

the first time we are iterating on the Matrix we do not have a "valid solution" to use that's why we need to take the "valid" position and add it into the queue to start iterating on the loop

keep the 2 `for` loops on the outside to keep traversing on the Matrix if we do not found a valid island yet

these problems reminds me to the ["Component" concept on Graphs](https://en.wikipedia.org/wiki/Component_(graph_theory))

### Source code (watch it only if we can't find a solution)

<details>
    <summary>Solution </summary>

```python
class Solution:
    def get_valid_ground(self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int) -> List:
        # Return new valid positions based on the current cell.
        # return List[ Tuple[int, int] ]
        n: int = len(grid)
        m: int = len(grid[0])
        out: List[List] = []

        # if visited[i][j] == False:
        #     out = [ [i, j] ]

        # Check right.
        if i < n and j + 1 < m and visited[i][j + 1] == False and grid[i][j + 1] == '1':
            out.append([i, j + 1])

        # Check down.
        if i + 1 < n and j < m and visited[i + 1][j] == False and grid[i + 1][j] == '1':
            out.append([i + 1, j])

        # Check left.
        if i < n and j - 1 >= 0 and visited[i][j - 1] == False and grid[i][j - 1] == '1':
            out.append([i, j - 1])

        # Check up.
        if i - 1 >= 0 and j < m and visited[i - 1][j] == False and grid[i - 1][j] == '1':
            out.append([i - 1, j])

        return out
    

    def numIslands(self, grid: List[List[str]]) -> int:
        islands: int = 0
        n: int = len(grid)
        m: int = len(grid[0])

        visited: List[List[bool]] = []
        for _ in range(0, n):
            visited.append( [ False for _ in range(0, m)] )

        valid_ground: List[List] = []

        for mi in range(0, n):

            for mj in range(0, m):

                if visited[mi][mj] == True:
                    continue

                if grid[mi][mj] == '0':
                    visited[mi][mj] = True
                    continue

                if grid[mi][mj] == '1':
                    valid_ground.append([mi, mj])

                small_island_size: int = 0

                while len(valid_ground) > 0:

                    new_ground: List = valid_ground.pop(0)

                    # Local indexes.
                    li, lj = new_ground[0], new_ground[1]
                    if visited[li][lj] == True:
                        continue

                    check_new_ground: List = self.get_valid_ground(grid, visited, li, lj)

                    # We may improve this part. Add non-visited possitions only.
                    valid_ground += check_new_ground

                    small_island_size += 1

                    visited[li][lj] = True

                if small_island_size > 0:
                    # New island found it.
                    islands += 1

        return islands
```

</details> 
