import math


class IntervalTree:
    def __init__(self, value: int, start: int, end: int, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.start = start
        self.end = end

    def common_part(self, given_start, given_end) -> bool:
        if given_end < self.start or given_start > self.end:
            return False
        return True

    def perfect_match(self, given_start, given_end) -> bool:
        if given_start == self.start and given_end == self.end:
            return True
        return False


def build_tree(nums: list) -> (IntervalTree, list):
    leafs = []
    for i, value in enumerate(nums):
        tmp = IntervalTree(value, i, i)
        leafs.append(tmp)

    level = leafs.copy()

    while len(level) != 1:
        new_level = []

        for i in range(0, len(level), 2):
            left_child = level[i]
            if i + 1 >= len(level):
                # skipping when odd elements
                new_level.append(left_child)
                break
            right_child = level[i + 1]

            tmp = IntervalTree(left_child.value + right_child.value, left_child.start, right_child.end, left_child,
                               right_child)
            left_child.parent = tmp
            right_child.parent = tmp
            new_level.append(tmp)
        level = new_level

    root = level.pop()
    return root, leafs


def tree_update(index: int, new_value: int, leafs: list) -> None:
    difference = new_value - leafs[index].value

    def change_value(node: IntervalTree):
        nonlocal difference
        node.value += difference
        if node.parent is not None:
            change_value(node.parent)

    change_value(leafs[index])


def tree_sum(root: IntervalTree, i: int, j: int) -> int:
    count = 0

    def sum_up(node: IntervalTree, i: int, j: int):
        nonlocal count
        if not node.common_part(i, j):
            return

        if node.perfect_match(i, j):
            count += node.value
            return

        sum_up(node.left, i, min(node.left.end, j))
        sum_up(node.right, max(node.right.start, i), j)

    sum_up(root, i, j)
    print(f'Found sum: {count}')
    return count


numbers = [0, 7, 5, 3, 1, 8, 6, 12, 3]
tree_root, tree_leafs = build_tree(numbers)
print(tree_root.value)
tree_update(3, 6, tree_leafs)
print(tree_root.value)

tree_sum(tree_root, 8, 8)
