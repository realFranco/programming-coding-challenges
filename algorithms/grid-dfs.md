## Grid DFS

### Description

Given a matrix (`n x m`) and a starting point, traverse the matrix using a DFS solution

### Notes

use recursion to traverse into a new position

use a list of directions to know where to go, is ok to start in any position, the next cell could up or left, etc.

using a boolean grid to mark visited positions, mark visited after print or process the node

### Algorithm

```python
from typing import List


DIRECTIONS: List[List[int]] = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]


tests = [
    [
        [-1,2,3],
        [0,9,8],
        [1,0,1]
    ],
]

def is_position_valid(n: int, m: int, cell: List[int]) -> bool:
    i, j = cell
    return 0 <= i < n and 0 <= j < m

def dfs(grid: List[List[int]], visited: List[List[int]], init: List[int], path: List[List[int]]) -> None:
    i, j = init
    print('cell:', grid[i][j])
    visited[i][j] = True

    for d in DIRECTIONS:
        pos_destiny: List[int] = [i + d[0], j + d[1]]

        if is_position_valid(len(grid), len(grid[0]), pos_destiny) == False:
            continue

        if visited[pos_destiny[0]][pos_destiny[1]] == True:
            continue

        dfs(grid, visited, pos_destiny, path)

for test in tests:
    n: int = len(test)
    m: int = len(test[0])

    visited = []
    for _ in range(n):
        visited.append([False for _ in range(0, m) ])

    path = []

    # Start vertex.
    # init = [0, 0]
    init = [2, 2]

    dfs(test, visited, init, path)
```
