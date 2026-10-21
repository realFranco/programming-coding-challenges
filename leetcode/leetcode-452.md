## 452. Minimum Number of Arrows to Burst Balloons

[leetcode link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

### Notes

we receive ranges, we have to sort them, incrementally using the left side and then right side of the left of the ranges are equal

we need to check if ranges are overlapped, we can measure that comparing two ranges, as the set of ranges where sorted we know the next ranges will be on the right from the current one

once we take a new range we need to check if that one could be inside or overlap on the current one, if that happen we must generate a new overlap, potentially shorter

iterate the solution on that logic

if the new range is not connected or overlapped with the current overlap on the left, then we need to generate a new overlap set (new overlap) and the upcoming ranges will be compared with new overlap

the return will be the groups length, which means the number of overlapped segments, at the end the number of arrows to use in order burst the balloons

### Source code (watch it only if we can't find a solution)

<details>
    <summary> Solution </summary>

```python
class Solution:
    def sort_points(self, points: List[List[int]]) -> List[List[int]]:
        return sorted(points, key=lambda p: (p[0], p[1]))

    def compute_overlap(self, current_overlap: List[int, int], new_range: List[int, int]) -> List[int, int]:
        new_left: int = current_overlap[0]
        new_right: int = current_overlap[1]

        if current_overlap[0] <= new_range[0] <= current_overlap[1]:
            new_left = new_range[0]

        if current_overlap[0] <= new_range[1] <= current_overlap[1]:
            new_right = new_range[1]
        
        out: List[int, int] = [new_left, new_right]

        return out

    def findMinArrowShots(self, points: list[list[int]]) -> int:
        i, j = 0, 0

        m: int = len(points)

        points = self.sort_points(points)

        group: List = []
        group.append( points[0] )

        while i < m - 1:

            if group[j][1] >= points[i+1][0]:

                local_overlap: List[int, int] = self.compute_overlap(group[j], points[i+1])

                group[j] = local_overlap

            else:
                # New overlap set.
                # Or new rage is not overlapped.
                group.append(points[i+1])

                j += 1

            i += 1

        return len(group)
```

</details>