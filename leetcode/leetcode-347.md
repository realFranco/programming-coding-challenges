## 347. Top K Frequent Elements

(leetcode link)[https://leetcode.com/problems/top-k-frequent-elements/description/].

### Notes

the solution i use do not implement queue / heaps, we could retake it

### Source Code (watch if we can't recreate the solution)

<details>
    <summary>Solution </summary>

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Store the frequency of each element.
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[n   um] += 1

        elements = [(num, frequency) for num, frequency in frequencies.items()]

        # Sort the list of tuples by frequency in descending order.
        elements.sort(key=lambda x: x[1], reverse=True)

        # Collect the 1st. element from the tuple.        
        return [e[0] for e in elements[:k]]

```

</details>
