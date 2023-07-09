from egz1btesty import runtests

"""
Znajdywana jest wyskosc drzewa, oraz dodawane jest skierowanie na rodzica oraz flaga
Potem znajdowane sa liscie drzewa i dodwane sa do list na odpowiedniej wysokosci
Wybierana jest najdluzsza lista lisci z najwieksza wysokosca
Przechodzi sie po lisciach , odcina sie ich dzieci zliczając ilosc uciętych krawedzi oraz z kazdego liscia 
idzie sie do góry zaznaczajacy droga na głownego korzenia (flaga ustawiania jest na True)
Odpalana jest funkcja która schodzi w dól jeżeli jest dziecko i ma ono ustawina flage na True, nieschodzi w dól
kiedy dziecko nie ma flagi True, oznacza to że jest to krawedz do odcięcia.

O(n)
"""


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # [Parent,flag]


def wideentall(T:Node) -> int:
    # tu prosze wpisac wlasna implementacje

    h = -1
    T.x = [None, False]

    def get_height(R: Node, level: int = 0) -> None:
        nonlocal h
        h = max(h, level)
        if R.left is not None:
            R.left.x = [R, False]
            get_height(R.left, level + 1)
        if R.right is not None:
            R.right.x = [R, False]
            get_height(R.right, level + 1)

    get_height(T)
    leafs = [[i] for i in range(h + 1)]

    def put_leafs(R: Node, level: int = 0) -> None:
        nonlocal leafs
        leafs[level].append(R)
        if R.left is not None:
            put_leafs(R.left, level + 1)
        if R.right is not None:
            put_leafs(R.right, level + 1)

    put_leafs(T)
    leafs.sort(key=lambda x: (len(x), x[0]), reverse=True)

    ans = 0

    def mark_paths(R: Node) -> None:

        if R.x[1] is True:
            return
        if R.x[0] is not None:
            R.x[1] = True
            mark_paths(R.x[0])

    for node in leafs[0][1:]:
        mark_paths(node)
        if node.left is not None:
            node.left = None
            ans += 1
        if node.right is not None:
            node.right = None
            ans += 1

    def erase(R: Node) -> None:
        nonlocal ans

        if R.left is not None:
            if R.left.x[1] is True:
                erase(R.left)
            else:
                ans += 1
                R.left = None
        if R.right is not None:
            if R.right.x[1] is True:
                erase(R.right)
            else:
                ans += 1
                R.right = None

    erase(T)

    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=False)

A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G

# print(wideentall(A))
