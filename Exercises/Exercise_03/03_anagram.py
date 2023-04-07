"""
Check in linear way whether 2 given words are anagrams

Anagram is a word formed by rearranging the letters of a different word
Listen == Silent
"""

"""
Solution requires creating array with 0 with all possible letters and going through words, where letters from
word A adds to array and letters from word B minus value in array, if array contains only 0 after the loop it mean
that words are anagrams
"""


def anagram(A: str, B: str) -> bool:
    n = len(A)
    arr = [0 for _ in range(26)]  # only lowercase letters

    for i in range(n):
        arr[ord(A[i]) - ord('a')] += 1
        arr[ord(B[i]) - ord('a')] -= 1

    for elem in arr:
        if elem != 0:
            return False
    return True


A = "listen"
B = "silent"
C = "scopes"

print(anagram(A, B))

print(anagram(A, C))
