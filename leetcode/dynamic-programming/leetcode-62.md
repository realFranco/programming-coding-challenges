## 62. Unique Path

[leetcode link](https://leetcode.com/problems/unique-paths/description/).

several time ago i observe this problem with another name, "Frog", same concept as this one

### Notes

grid `n x m`

frog start in `0, 0` and must visit `n-1, m-1` position

frog can move only left and right

a hint:

- how many moves can the frog do to reach the target position ?

the next youtube video explains several DP patters, one of them (the last one) explains how to
tackle this problem

[YouTube link](https://youtu.be/Hdr64lKQ3e4?si=jwCGc959U4oZVoX5).

similar to [LeetCode 64](./leetcode-64.md)

### Source Code (watch iif we can't recreate the solution)

<details>
    <summary>Solution </summary>

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def frog_moves(dp: list[list[int]]) -> int:
            n: int = len(dp)
            m: int = len(dp[0])

            # Set the top-left corner with `1`.
            # dp[0][0] = 1
        
            # # Fill the rows.
            # for j in range(1, m):
            #     dp[0][j] = 1

            # # Fill the columns.
            # for i in range(1, n):
            #     dp[i][0] = 1

            for i in range(1, n):
                for j in range(1, m):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

            return dp[n-1][m-1]

        
        # Build the grid.
        dp: list[list[int]] = [ [1] * n for _ in range(m)]

        out: int = frog_moves(dp)

        return out
```

</details>
