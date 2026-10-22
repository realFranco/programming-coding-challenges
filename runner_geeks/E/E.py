"""
Execution example.

python3 E.py < input
"""
import copy
from math import factorial
from typing import List


def permutation(n: int, sol: list, t_sol: list, end: bool) -> list:
    i = 0
    while i < n and end == False:
        i += 1
        if i not in t_sol:
            t_sol.append(i)
            if len(t_sol) == n:
                sol.append(copy.copy(t_sol))
                if len(sol) == factorial(n):
                    end = True

            permutation(n, sol, t_sol, end)
            t_sol.pop()
    
    return sol


if __name__ == '__main__':
    
    n = int(input())
    # I am not using the array from the input.
    _ = input()  
    sol, t_sol = [], []
    end = False

    out = permutation(n, sol, t_sol, end)
    for permute in out:
        print(
            ' '.join([str(_) for _ in permute])
        )
