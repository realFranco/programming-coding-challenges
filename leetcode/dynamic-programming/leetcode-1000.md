## 1000. Merge stones

[leetcode link](https://leetcode.com/problems/minimum-cost-to-merge-stones/description/).

### Notes

### Source Code (watch iif we can't recreate the solution)

<details>
    <summary>Solution </summary>

```python
# My greedy solution, invalid one.
class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        n: int = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        grid: list[int][int] = [[0 for _ in range(n)] for _ in range(n)]
        stones_counter: int = n
        smaller_merge: float = float("inf")
        for i in range(0, len(stones)):
            grid[i][i] = stones[i]

        out: list[int] = []
        while stones_counter > 1:

            for i in range(0, stones_counter-k+1):
                # Merge the stones.
                merges: list[int] = [grid[i_range][i_range] for i_range in range(i, i+k)]
                
                merges_result: int = sum(merges)
                if merges_result < smaller_merge:
                    smaller_merge = merges_result
                    # Store the value and the index.
                    grid[i][i+1] = merges_result
                    smaller_merge_index = [i, i+1]

            stones_counter -= (k-1)

            x, y = smaller_merge_index
            out.append(grid[ x ][ y ])  # Store solution.

            # We will convert into zero the stones we merge.
            for i_clean in range(x, x+k):
                grid[i_clean][i_clean] = 0

            # Move the minimum merge into the main diagonal.
            grid[x][y-1] = grid[x][y]

            # Move diagonal k-1 movement to the top left.
            for i_swap in range(x + 1, n):
                if i_swap+k-1 < n:
                    grid[i_swap][i_swap], grid[i_swap+k-1][i_swap+k-1] = grid[i_swap+k-1][i_swap+k-1], grid[i_swap][i_swap]

            # Restart tje smaller merge as the stones set is a new one.
            smaller_merge = float("inf")

        return sum(out)
```

```python
# See: https://algo.monster/liteproblems/1000.

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
      
        # Check if it's possible to merge all stones into one pile
        # We need exactly (n-1)/(K-1) merge operations
        if (n - 1) % (K - 1) != 0:
            return -1
      
        # Build prefix sum array for quick range sum calculation
        # prefix_sum[i] = sum of stones[0] to stones[i-1]
        prefix_sum = [0]
        for stone in stones:
            prefix_sum.append(prefix_sum[-1] + stone)
      
        # dp[i][j][m] = minimum cost to merge stones[i-1] to stones[j-1] into m piles
        # Initialize with infinity (impossible states)
        dp = [[[float('inf')] * (K + 1) for _ in range(n + 1)] for _ in range(n + 1)]
      
        # Base case: single stone forms 1 pile with cost 0
        for i in range(1, n + 1):
            dp[i][i][1] = 0
      
        # Iterate over all possible subarray lengths
        for length in range(2, n + 1):
            # Iterate over all possible starting positions
            for start in range(1, n - length + 2):
                end = start + length - 1
              
                # Try to form different number of piles
                for num_piles in range(2, K + 1):
                    # Try different split points
                    for split in range(start, end, K - 1):
                        # Merge left part into 1 pile and right part into (num_piles - 1) piles
                        dp[start][end][num_piles] = min(
                            dp[start][end][num_piles],
                            dp[start][split][1] + dp[split + 1][end][num_piles - 1]
                        )
              
                # Merge K piles into 1 pile
                # The cost is the sum of all stones in the range
                dp[start][end][1] = dp[start][end][K] + prefix_sum[end] - prefix_sum[start - 1]
      
        # Return minimum cost to merge all stones into 1 pile
        return dp[1][n][1]
```
</details>
