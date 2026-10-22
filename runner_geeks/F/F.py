"""
Execution example.

python3 F.py < input
"""
def horner(a, i, n, x) -> None:
    if i < n:    
        return a[i] + x * horner(a, i+1, n, x)
    
    return a[n]


if __name__ == '__main__':

    n = int(input())
    a = [int(_) for _ in input().split(' ')]
    x = int(input())
    i = 0
    
    out = horner(a, i, n, x)
    print(out)
