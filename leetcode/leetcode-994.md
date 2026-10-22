## 994. Rotting Oranges

[leetcode link](https://leetcode.com/problems/rotting-oranges/)

### Notes

i observe the solution from NeetCode in YTB as i do not find a solution on my 3rd. try

we need to collect all the Rotten Oranges, those where cell values is 2

we need to count the Fresh Oranges, those where cell values is 1

we need to BFS starting from the Rotten Oranges, for that we just collect valid neighbors from
Rotten Oranges
add those values into a queue

we need to iterate until the queue comes empty or the fresh oranges becomes 0

there is an inner `for` loop that will iterate on the valid positions only

each time Fresh Orange is visited, we decrease the fresh counter as well

a key part is that we need to collect the size of the queue before been updated `iters = len(q)`
once the for loop that runs `iters` times ends, we then mark that as "one minute" pass

as the internal `for` loop will keep adding positions, the external `while` loop can continue

### Source code (watch it only if we can't find a solution)

<details>
    <summary> Solution </summary>

```python
from collections import deque()


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while q and fresh > 0:
            iters = len(q)
            for _ in range(iters):
                i, j = q.popleft()

                for di, dj in directions:
                    row, col = di + i, dj + j

                    if (row < 0 or row == n or col < 0 or col == m or grid[row][col] != 1):
                        continue

                    grid[row][col] = 2
                    fresh -= 1

                    q.append([row, col])

            time += 1

        return time if fresh == 0 else -1
```

</details>
