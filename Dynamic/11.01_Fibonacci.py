# O(n)
def fib(n: int) -> int:
    if n < 2:
        return 1

    F = [0 for _ in range(n + 1)]
    F[0] = 1
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]


n = 6

print(fib(n))
