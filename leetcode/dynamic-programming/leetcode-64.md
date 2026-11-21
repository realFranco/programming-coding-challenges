## 64. Minimum Path Sum

[leetcode link](https://leetcode.com/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=dynamic-programming).

i try the challenge several times until i get some hints using Gemini (LLM), i do not request for the final result i just provide my solution (failing ones) and ask fkr hints, iterate and got a valid result

my initial solution was a Greedy / DFS with weight matrix, so i have to re-compute several steps

i took this challenge (i can classified as Medium-Easy) to keep adding more foundational layers about DP as currently i am still thinking in these problems like Graph Traversals ones

see my own notes using a deck:

[LeetCode 64 - Oxford deck (PDF)](../../algorithms/dynamic-programming/leetcode-64-oxford-deck.pdf).

### Notes

couple of edge cases:

- first position in the DP matrix is the same as the grid matrix

- the first row will take values from the first row only

- the first column will take values form the first column only

one the edge cases where applied iterate the grid

to populate a position inside the dp matrix use the min between the previous left and previous up position and sum the current position from the grid (weight)
to indicate that reach those indexes the minimum cost will be the minimum neighbor plus the current weight to get there

### Source Code (watch iif we can't recreate the solution)

<details>

<summary>Solution </summary>

```python
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        def traverse_dp(grid, dp) -> None:
            n: int = len(grid)
            m: int = len(grid[0])

            dp[0][0] = grid[0][0]

            # Row is 0.
            for j in range(1, m):
                dp[0][j] = grid[0][j] + min(dp[0][j], dp[0][j-1])

            # Column is 0.
            for i in range(1, n):
                dp[i][0] = grid[i][0] + min(dp[i][0], dp[i-1][0])

            for i in range(1, n):
                for j in range(1, m):
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        i: int = len(grid) - 1
        j: int = len(grid[0]) - 1

        dp: list = [ [ float("inf") ] * (j+1) for _ in range(i+1) ]
        traverse_dp(grid, dp)
        out: int = dp[-1][-1]

        return out
```
</details>
