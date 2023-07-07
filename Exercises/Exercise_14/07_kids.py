"""
Group of n children play at building as large a tower as possible. Each child has blocks of different heights.
The children have just gone to eat dessert, but one child is left behind. Now he has the only opportunity to pick up a
few blocks from the other children so that his tower is the highest. The number of blocks taken must be minimal.
"""

"""
Greedy
Child steels till its towers isnt the biggest. It take biggest box from child with highest tower currently.
"""


def kids(C: list, thief: int) -> int:
    n = len(C)

    towers = [sum(C[i]) for i in range(n)]
    stolen = 0
    while towers[thief] != max(towers):

        index = best = -1
        for i, value in enumerate(towers):
            if i != thief and best < value:
                index = i
                best = value

        biggest_block = max(C[index])
        towers[index] -= biggest_block
        C[index].remove(biggest_block)
        towers[thief] += biggest_block

        stolen += 1

    print(towers)
    return stolen


children = [[2, 3, 9], [1, 1], [2, 3, 10], [4, 4, 4], [6, 7, 7]]
thief = 1
print(kids(children, thief))
