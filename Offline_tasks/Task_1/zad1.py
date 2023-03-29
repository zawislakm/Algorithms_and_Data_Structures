from zad1testy import runtests

"""
Maksymilian Zawiślak, 410609
Algorithm check all the possible solutions, i is as middle of palindrome and while loop adds next character 
neighbors (k parameter, k starts from 1 because i - 0 == i ) 
on left and right, till they are different or [(i-k), (i+k)] are out of band 
"""


def ceasar(s: str) -> int:
    ans = 0
    n = len(s)
    for i in range(n):
        k = 1
        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
            k += 1
        ans = max(ans, 2 * k - 1)
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
