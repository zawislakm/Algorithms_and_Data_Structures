import math

from egz1btesty import runtests

"""
#Maksymilian Zawislak 410609

Tablica dynamic rozmiaru (nE) zawiera minmalny koszt dojazdu do danej planety zawierajac jeszcze b paliwa.

Wypleniania jest pokoleji, napierw jest dodanie teleportu z kosztu dojazdu zerowego
Natepnie ustawiane sa koszty dojazdu do nastepnej stacji.
Ustawiany jest koszt dojechania z e iloscia paliwa do niej.
Obliczany jest na podstawie wczesneijszych dojazdów do tablicy, wybierany jest minalny koszt dojazdu
patrzac na dojazdy zawierajace odpowienida ilosc paliwa.

O(n*E*E)
"""


# def planets(D, C, T, E):
#       # O(n^2E^2)
#     # tu prosze wpisac wlasna implementacje
#
#     n = len(D)
#     dynamic = [[math.inf for _ in range(E + 1)] for _ in range(n)]
#     dynamic[0][0] = 0
#
#     for i in range(n - 1):
#         dynamic[T[i][0]][0] = min(dynamic[i][0] + T[i][1], dynamic[T[i][0]][0])  # kosz portalu
#
#         for j in range(i + 1, n):  # wierzcholki do przodu
#             if D[j] - D[i] <= E:  # sprawdzenie czy da sie dojechac na pelnym baku do j
#                 for e in range(E + 1):  # dojechanie do wierzcholka j majac jeszcz e paliwa
#                     if e + (D[j] - D[i]) <= E:  # sprawdznie czy jest to mozliwe
#                         k = 0
#                         while k <= e + (D[j] - D[i]):  # wybiranie ile zatankowac a ile zabrac ze wczesneijszego baku
#                             dynamic[j][e] = min(dynamic[j][e], dynamic[i][k] + C[i] * (e + (D[j] - D[i]) - k))
#                             k += 1
#
#     return dynamic[n - 1][0]  # mozna zwaracac taki wyniki bo nie oplaca sie przyjezdzac do B majac cos jeszcze w baku


def planets(D: list, C: list, T: list, E: int) -> float:
    # tu prosze wpisac wlasna implementacje

    n = len(D)
    dynamic = [[math.inf for _ in range(E + 1)] for _ in range(n)]
    dynamic[0][0] = 0

    for i in range(n - 1):
        dynamic[T[i][0]][0] = min(dynamic[i][0] + T[i][1], dynamic[T[i][0]][0])  # kosz portalu

        j = i + 1  # natepny wierzcholek
        for e in range(E + 1):  # dojechanie do wierzcholka j majac jeszcz e paliwa
            if e + (D[j] - D[i]) <= E:  # sprawdznie czy jest to mozliwe
                k = 0
                while k <= e + (D[j] - D[i]):  # wybiranie ile zatankowac a ile zabrac ze wczesneijszego baku
                    dynamic[j][e] = min(dynamic[j][e], dynamic[i][k] + C[i] * (e + (D[j] - D[i]) - k))
                    k += 1

    return dynamic[n - 1][0]  # mozna zwaracac taki wyniki bo nie oplaca sie przyjezdzac do B majac cos jeszcze w baku


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
