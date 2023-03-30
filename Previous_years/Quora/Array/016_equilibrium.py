from typing import List


def find_equilibrium(A: List[int]) -> List[int]:
    ans = []
    n = len(A)
    sub = [0 for _ in range(n)]
    sub[0] = A[0]
    for i in range(1, n):
        sub[i] = A[i] + sub[i - 1]

    if sub[0] == 0 and sub[n - 1] == sub[0]:
        ans.append(0)
    if sub[n - 1] == 0 and sub[n - 1] == sub[n - 2]:
        ans.append(n - 1)

    for i in range(1, n - 1):
        if sub[i - 1] == sub[n - 1] - sub[i]:
            ans.append(i)

    return ans


array = [0, -3, 5, -4, -2, 3, 1, 0]
# array = [0, 3, 5, -4, 3, 5, 0]
print(find_equilibrium(array))
