## 1143. Longest Common Subsequence

[leetcode link](https://leetcode.com/problems/longest-common-subsequence/description/).

### Notes

i do not save information about the code i generate, i remember that after several tries i got into a YouTube solution

i am generating the notes around 3 weeks after i pass the solution on LeetCode, the elements i remember:

- as you can imagine, the solution will required DP (Grid) attempt from top to bottom
- one of the words will be in the column and the other one as a row
- internally there is a condition that will count if the words are the same or not

YouTube that show us the solution:

[YouTube link](https://youtu.be/NnD96abizww?si=pWwnogAVjq6foSUJ) (thanks Tushar !, was an interesting solution).

### Source Code (watch iif we can't recreate the solution)

<details>
    <summary>Solution </summary>

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def get_longest_common_subsequence(str1: str, str2: str) -> int:
            """
            Receive two strings.

            :return int. Length of the longest common subsequence.
            """
            n: int = len(str1)
            m: int = len(str2)

            # TODO: Check boundaries.

            # Building the grid containing the weights of appearance.
            dp: list[list[int]] = [[0] * (m+1) for _ in range (n+1)]

            # i will index in function of str1.
            # j will index in function of str2.
            for i in range(1, n+1):
                for j in range(1, m+1):

                        # print(str1[i], str2[j])

                        if str1[i - 1] == str2[j - 1]:
                            # Match: extend cleanly from the diagonal
                            dp[i][j] = dp[i - 1][j - 1] + 1

                        else:
                            dp[i][j] = max( dp[i-1][j], dp[i][j-1] )
            
            return dp[n][m]

        out: int = get_longest_common_subsequence(text1, text2)

        return out
```

</details>
