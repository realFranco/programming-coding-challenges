## 68. Text Justification

[leetcode link](https://leetcode.com/problems/text-justification/description/).

### Notes

[youtube link](https://www.youtube.com/watch?v=RORuwHiblPc) (thanks Tushar !, was an interesting
solution).

this particular leetcode is not optimal for technical interviews as must be done using an
"optimal-way" there is no room for discuss "less optimal" solution

another website that i found interesting to is this one:

[algodaily - Test Justification](https://algodaily.com/challenges/text-justification).

### Source Code (watch iif we can't recreate the solution)

<details>
    <summary>Solution </summary>

```python
"""
notes i introduce into the leet code challenges:

i watch this video: 

https://www.youtube.com/watch?v=RORuwHiblPc. 

differences:

the way i calculate the lines is diferent

i use a heap to calculate the "optimal" end of the line

i struggle a little bit while add the "empty spaces" on the line, i have to tackle 3 edges cases.

i will push this into my GitHub Repository

https://leetcode.com/problems/text-justification/description/

leetcode 68
"""


import heapq
from typing import List, Tuple

tests = [

    [
        ["Nissan", "GTR", "Nismo", "IV", "Toyo"],
        10
    ],

    [
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16
    ],

    [
        ["This", "is", "an", "example", "of", "text", "justification"],
        16
    ],

]

class DPTextJustificationv1:

    # See: https://algodaily.com/challenges/text-justification.

    # Cost function.
    def f(self, i: int, j: int, words: list[str], pageWidth: int, n: int) -> int:
        misFit: int = 0

        lineLen = -1

        infValue = float("inf")

        # for ind in range(i, j + 1):
        #     if lineLen <= pageWidth:
        #         lineLen = lineLen + len(ind) + 1

        lineLen: int = sum( [len(words[_]) for _ in range(i, j + 1)] )

        if lineLen > pageWidth:
            misFit = infValue
        else:
            misFit = int( pow((pageWidth - lineLen), 3) )

        if j == n -1 and misFit != infValue:
            return 0

        return misFit
            

    def getDP(self, words: list[str], dp: list[int], split: list[int], pageWidth: int, i: int) -> None:
        if i >= len(dp):
            return 0

        if dp[i] != -1:
            return dp[i]

        n: int = len(dp)

        infValue: float = float("inf")

        min: float = infValue

        minInd: int = 0

        misFit: int = 0

        for j in range(i, n):

            if misFit < infValue:
                misFit = self.f(i, j, words, pageWidth, n) + self.getDP(words, dp, split, pageWidth, j + 1)

                if (misFit < min):
                    min = misFit
                    minInd = j

        dp[i] = min
        split[i] = minInd

        return dp[i]

# Applying a new solution.
def compute_grid_of_weights(grid: list[list[int]], words: list[str], pageWidth: int) -> None:
    n: int = len(words)

    for i in range(0, n):

        for j in range(i, n):

            # w = words[i: j+1]
            width = len( ' '.join(words[i: j+1]) )

            if width > pageWidth:
                # Current word can't fit in the line. We can continue from the next word.
                break

            grid[i][j] = pow(pageWidth - width, 2)


def compute_line_breaks(grid: list[list[int]]) -> list[int]:
    n: int = len(grid)
    brake_lines_set: List[Tuple[int, int]] = [] # Tuple <weight, j-index>

    for i in range(0, n):
        brake_lines_set.append([])

        for j in range(i, n):
            weight: int = grid[i][j]

            if weight == -1:
                continue

            brake_lines_set[i].append( (weight, j) )

        heapq.heapify(brake_lines_set[i])

    # Generate the final list of break lines collecting the first
    break_lines: list[int] = [ brake_lines_set[_][0][1] for _ in range(n) ]
    
    return break_lines


def middle_computation_of_words(words: list[str], break_lines: list[int], pageWidth: int) -> list[list[str]]:
    n: int = len(words)
    lines: list[list[str]] = []
    additional_spaces_in_line: list[int] =[]

    previous_most_right_index: int = -1
    for i in range(0, n):

        # We want new positions.
        if i <= previous_most_right_index:
            continue
        
        i, j = i, break_lines[i]
        temp_line = []

        for _ in range(i, j + 1):
            temp_line.append( words[_] )
        lines.append(temp_line)

        width: int = pageWidth - len( ' '.join(temp_line) )
        additional_spaces_in_line.append(width)
        # print('Line', temp_line, ' will need ', width, ' spaces [Greedy-left-to-right]')

        previous_most_right_index = j

    for i in range(len(lines)):
        counter: int = additional_spaces_in_line[i]
        if counter == 0:
            continue

        # Last line will receive the white spaces at the very right.
        # If line contains one word only, add spaces at the very right.
        if i == len(lines) - 1 or len(lines[i]) == 1:
            lines[i][-1] += ' ' * counter
            continue

        # Greedy to add lines from left to right.
        n = len(lines[i])
        while counter > 0:
            for j in range(n):
                if counter == 0:
                    break

                if j == n - 1:
                    continue
                lines[i][j] += ' '
                counter -= 1

    return lines


for test in tests:
    words: list[str] = test[0]
    pageWidth: int = test[1]

    # dp: list[int] = [-1] * len(words)
    # split: list[int] = [-1] * len(words)
    # start: int = 0
    # DPTextJustificationv1().getDP(words, dp, split, pageWidth, 0)

    grid: list[list[int]] = [ [ -1 for  _ in range(len(words)) ] for _ in range(len(words)) ]

    compute_grid_of_weights(grid, words, pageWidth)

    # Create the line breakers from grid.
    break_lines: int = compute_line_breaks(grid)

    # I just want to observe the current lines.
    lines:list[list[str]] = middle_computation_of_words(words, break_lines, pageWidth)
    for l in lines:
        print(f'{' '.join(l)}|')
    # Calculate the additional spaces we need to add (Greedy method from left to right).
    # Last line will add all the elements to the right.

    print('---.\n\n')
```
</details>
