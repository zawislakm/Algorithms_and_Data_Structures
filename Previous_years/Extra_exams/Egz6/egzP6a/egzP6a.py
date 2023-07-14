from egzP6atesty import runtests

"""
Nie ma sortowania po tych zasadach.

Najpierw dzieli sie na kubelki po dlugosci slowa
potem szuka sie kubelka w którym znajduje sie slowo na zadanym s
Ten kubelek dzieli sie na kubelki po ilosci liczb
potem szuka sie kubelka w którym znajduje sie slowo na zadanym s

"""


def nums(S: str) -> int:
    ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    counter = 0
    for e in S:
        if e in ints:
            counter += 1
    return counter


def google(H, s):
    # tutaj proszę wpisać własną implementację

    n = 0
    for i in H:
        n = max(n, len(i))

    length_buckets = [[] for _ in range(n)]

    for i in H:
        length_buckets[n - len(i)].append(i)

    i = 0
    c = 0
    while c + len(length_buckets[i]) < s:
        c += len(length_buckets[i])
        i += 1

    s -= c

    number_buckets = [[] for _ in range(len(length_buckets[i][0]) + 1)]

    for e in length_buckets[i]:
        number_buckets[nums(e)].append(e)

    i = 0
    c = 0

    while c + len(number_buckets[i]) < s:
        c += len(number_buckets[i])
        i += 1


    return number_buckets[i][0]

runtests ( google, all_tests=True )


H = ["aba", "abc", "ab1", "abab", "a1a1", "aa12a"]
s = 3
google(H, s)
