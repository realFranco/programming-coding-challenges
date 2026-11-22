## 911. Online Election

[leetcode link](https://leetcode.com/problems/online-election/).

### Notes

- do think too much about the time, just use each iteration as the moment when we receive the votes
- think in sort the votes every time a new vote arrive
- store the last one (winner) on that point in time
- first problem i partially solve after my Exams ! (feel mostly proud as i was forgetting to solve this challenges)
- the sorting needs to be done using a Binary Tree way, using the indexes and `(lo + hi ) // 2` math operation

### Source Code (watch iif we can't recreate the solution)

```python
tests = [

    [
        ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"],
        [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]

    ]

]

# retrieve the max (most recent person with that max) by time
# so we can "query" them

def frequency(votes: list[int], times: list[int]) -> list:
    # {k: int person_i, v: Tuple (number of votes, time when the vote was applied)}
    persons: dict[int, int] = {}

    results = []

    for i in range(0, len(votes)):

        # for vote in votes:
        vote: int = votes[i]
        time: int = times[i]

        if vote not in persons:
            persons[vote] = (1, time)
        else:
            persons[vote] = (persons[vote][0] + 1, time)

        # sort the dictionary based on the votes
        # query_map[time] = sort(lambda)

        persons_list = [(k,v) for k, v in persons.items() ]
        persons_list.sort(key=lambda x: x[1])

        print()

        results.append(persons_list[-1])

    return results

def query(t: int, times: list[int], results: list) -> int:
    lo, hi = 0, len(times) - 1
    idx = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if times[mid] <= t:
            idx = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return results[idx] 

for test in tests:
    PROCESS_DATA: str = 'TopVotedCandidate'
    QUERY_DATA: str = 'q'

    operations: list[str] = test[0]
    votes, time = test[1][0]
    queries: list = test[1][1:]

    result: list[int] = []

    # flat the queries using a "monoid".
    queries = sum(queries, [])

    for op in operations:
        if op == PROCESS_DATA:
            result_by_persons: list = frequency(votes, time)
            result_by_persons = [_[0] for _ in result_by_persons]
            
        elif op == QUERY_DATA:
            out = query(queries.pop(0), time, result_by_persons)
            result.append(out)

        else:
            continue

    print('result', result)
```

### Source Code we introduce in LeetCode

```python
class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        # {k: int person_i, v: Tuple (number of votes, time when the vote was applied)}
        persons_in: dict[int, int] = {}

        self.results = []
        self.votes = persons
        self.times = times

        for i in range(0, len(self.votes)):

            # for vote in votes:
            vote: int = self.votes[i]
            time: int = self.times[i]

            if vote not in persons_in:
                persons_in[vote] = (1, time)
            else:
                persons_in[vote] = (persons_in[vote][0] + 1, time)

            # sort the dictionary based on the votes and arrival time.
            persons_list = [(k,v) for k, v in persons_in.items() ]  # O(n)
            persons_list.sort(key=lambda x: x[1])  # O(n)

            self.results.append(persons_list[-1])

            self.results

    # I required help for this, I knew that I can use a Bin Tree search
    # but i wasn't sure how to implemented it.
    def q(self, t: int) -> int:
        lo, hi = 0, len(self.times) - 1
        idx = -1
        while lo <= hi:  # O(log(n))
            mid = (lo + hi) // 2
            if self.times[mid] <= t:
                idx = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return self.results[idx][0] 

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```
