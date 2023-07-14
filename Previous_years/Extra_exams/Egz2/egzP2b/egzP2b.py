import math

from egzP2btesty import runtests
from math import log10

"""
Drzewo binarne tworzy wszytkie slowa z D idac w doł od konca,
Na kazdym miniętym wezle zwiększajc wartosc value o 1.
Wezel oznacza ile jest takich słow konczacych sie na zadany sufix

Potem idąc po slowach z tablic Q szukany jest wezel pasujacego slowa i zlicana jest suma z math.log10(value)
"""


class BST:

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = 0


def kryptograf(D: list, Q: list) -> float:
    # tutaj proszę wpisać własną implementację

    root = BST()

    def build_tree(s: str, node: BST, prev: BST = None):
        node.value += 1
        node.parent = prev
        if s == "":
            return
        if s[-1] == "0":
            if node.left is None:
                new_node = BST()
                node.left = new_node
            build_tree(s[:-1], node.left, node)
        if s[-1] == "1":
            if node.right is None:
                new_node = BST()
                node.right = new_node
            build_tree(s[:-1], node.right, node)

    for s in D:
        build_tree(s, root)

    ans = 0

    def count_tree(s: str, node: BST):

        if s == "":
            nonlocal ans
            ans += math.log10(node.value)
            return

        if s[-1] == "0":
            count_tree(s[:-1], node.left)
        if s[-1] == "1":
            count_tree(s[:-1], node.right)

    for s in Q:
        count_tree(s, root)

    return ans


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=3)

D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]

kryptograf(D, Q)
