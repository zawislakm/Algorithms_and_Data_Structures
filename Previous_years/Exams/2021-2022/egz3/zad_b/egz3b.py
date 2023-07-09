from egz3btesty import runtests

"""
# O(n^2)

Dwie tablice, NxN
From_up - oznacza ilosc mnietych komnat idac od góry
From_down - oznacza ilosc minietych komnat idac od dolu

Pierwsza kolumna z From_up jest uzupelnania z pola (0,0), from_down nie moze byc bo nie ma takiego dojscia

prev(row,column) to maksymalana wartosci z tego samego row i wczesniejszej kolumny z obu tablic

Nastepnie petla idąca od pierwszej do ostatniej komolumny
Na pozycjach [0][columna] dla from_up oraz [n-1][columna] dla from_down ustalany jest prev + 1, jezeli da sie tam wejsc
(robi sie to tak zeby problemu z indexem -1 oraz n nie bylo problemu)

Potem dwie petle:

Idaca od 1 do N uzupelnia table From_up maksymalna( wartosc z preva lub komnaty powyzej) + 1

Idaca od n-2 do -1 uzupelna tabele From_down maksymalana (wartosc z preva lub komnaty ponizej) + 1

Wynik to max z obu tablica dla pozycji [n-1][n-1]
"""


def maze(L: list) -> int:
    # tu prosze wpisac wlasna implementacje
    n = len(L)
    # takie duze minusy zeby wyniki sie zgadzaly dla jakis prevów dziwnych
    from_up = [[-10000 for _ in range(n)] for _ in range(n)]
    from_down = [[-10000 for _ in range(n)] for _ in range(n)]

    from_up[0][0] = 0

    for i in range(1, n):
        if L[i][0] == "#":
            break
        else:
            from_up[i][0] = 1 + from_up[i - 1][0]

    def prev(row, column):
        return max(from_up[row][column - 1], from_down[row][column - 1])

    for column in range(1, n):

        # edge cases
        if L[0][column] == ".":
            from_up[0][column] = prev(0, column) + 1
        if L[n - 1][column] == ".":
            from_down[n - 1][column] = prev(n - 1, column) + 1

        # loop to fill from_up
        for row in range(1, n):
            if L[row][column] == ".":
                from_up[row][column] = max(prev(row, column), from_up[row - 1][column]) + 1
        # loop to fill from_down
        for row in range(n - 2, -1, -1):
            if L[row][column] == ".":
                from_down[row][column] = max(prev(row, column), from_down[row + 1][column]) + 1

    result = max(from_up[n - 1][n - 1], from_up[n - 1][n - 1])
    return result if result > 0 else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
