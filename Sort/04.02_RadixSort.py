from typing import List


# nt
# n number of words, t length of the longest word
# stable
def countingsort(A: List[str], k: int, index: int) -> None:
    n = len(A)
    C = [0] * k
    B = [None] * n

    for i in range(n):
        C[ord(A[i][index]) - 97] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[ord(A[i][index]) - 97] -= 1
        B[C[ord(A[i][index]) - 97]] = A[i]

    for i in range(n):
        A[i] = B[i]


def radix_sort(arr: List[str]) -> None:
    k = 26  # only 25 letters in alphabet
    t = len(arr[0])
    for index in range(t - 1, -1, -1):
        countingsort(arr, k, index)


arr = ["kra", "art", "kot", "kit", "ati", "kil"]
print(arr)
radix_sort(arr)
print(arr)
