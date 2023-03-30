import queue


def mergesort(A: list, p: int) -> None:
    if len(A) < 2:
        return
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    mergesort(left, p)
    mergesort(right, p)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i][p] < right[j][p]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


def overlapping(A: list) -> list:
    n = len(A)
    mergesort(A, 1)
    mergesort(A, 0)
    print(A)

    flag = True
    while flag:
        flag = False
        ar = []
        i = 0
        while i < len(A):
            if i + 1 == len(A):
                ar.append(A[i])
                break
            if A[i][1] >= A[i + 1][0]:
                flag = True
                ar.append([A[i][0], max(A[i + 1][1], A[i][1])])
            else:
                ar.append(A[i])
                ar.append(A[i + 1])
            i += 2
        A = ar
    # //print(A)
    return A


array = [[1, 5], [2, 3], [4, 6], [7, 8], [8, 10], [12, 15]]
print(overlapping(array))
