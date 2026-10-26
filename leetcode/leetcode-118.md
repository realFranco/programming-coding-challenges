## 118. Pascal's Triangle

[leetcode link](https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=dynamic-programming)

### Notes

the solution i implement could be improved a lot

the triangle is "manually" create on the first 2 levels
the triangle is partially created we create the triangle from the biggest numbers to the right:

lvl 2, `1 1`
lvl 3, `2 1`
lvl 4 `3 3 1`
lvl 5 `6 4 1`
lvl 6 `10 10 5 1`

we use this ideas as some parts of each level are duplicates, so i decide to do not compute it

we use an iterative solution:

- from the previous level construct the current level
- the `ith` on the current level is the sum of the `i` and `i+1` from the previous level
- we found that in every number that is a multiple of 2 we must repeat the first position of the
array, e. g.,

lvl 2, `1 1`
lvl 4 `3 3 1`
lvl 6 `10 10 5 1`

there is a common step that is replicated in every level which is the insertion of the last `1`

then we create a function which is named `complete_triangle()`, we will explain using some inputs
and outputs examples

input: 
lvl 2, `1 1`
lvl 4 `3 3 1`
lvl 6 `10 10 5 1`

output:
lvl 2, `1 1`
lvl 4 `1 3 3 1`
lvl 6 `1 5 10 10 5 1`

we basically use a `while` loop were we insert:

- the nth element on the 1st. position
- the the n-1 on 2nd. position
- and so on ...

later than that we return the `triangle` Python list object, or just print it in case you want to
observe it

### Source Code (watch iif we can't recreate the solution)

<details>
    <summary>Solution </summary>

```python
tests = [
    1,
    5,
    6,
    7,
    12,
]

def pascal(triangle: list, max_lvl: int) -> None:

    for current_lvl in range(1, max_lvl + 1 ):

        triangle.append([])

        if current_lvl < 3:
            triangle[current_lvl-1] = [1]

        if current_lvl >= 3:

            for i in range(0, len(triangle[current_lvl-2])-1):
                triangle[current_lvl-1].append( triangle[current_lvl-2][i] + triangle[current_lvl-2][i+1] )

            # Replicate the 1st. position.
            if current_lvl % 2 == 0:
                triangle[current_lvl-1].insert(0, triangle[current_lvl-1][0])

        if current_lvl > 1:
            triangle[current_lvl-1].append(1)
    
def complete_triangle(triangle: list[list[int]]):
    # 0-based index.
    triangle_lvl: int = len(triangle)

    for current_lvl in range(0, triangle_lvl):

        front_index: int = 1
        while len(triangle[current_lvl]) < current_lvl + 1:
            # Copy the nth to the front while the condition be ok.
            
            triangle[current_lvl].insert(front_index-1, triangle[current_lvl][-front_index])
            front_index += 1

def cute_print(triangle: list[list[int]]):
    max_lvl: int = len(triangle)

    for lvl in triangle:
        spaces: str = (max_lvl - len(lvl)) * ' '
        line: str = ' '.join([str(_) for _ in lvl])
        print( spaces + line)

for n in tests:
    triangle: list[list[int]] = []
    pascal(triangle, max_lvl=n)

    complete_triangle(triangle)

    # print(triangle)

    cute_print(triangle)

    print('\n\n')
```
</details>
