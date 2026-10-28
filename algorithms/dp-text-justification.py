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
        11
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

    print('end')

