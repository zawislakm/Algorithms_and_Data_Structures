from egzP4btesty import runtests


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def prev_BST(root: Node) -> Node:
    if root.left is not None:
        # child on one left and max deep right
        root = root.left
        while root.right is not None:
            root = root.right
        return root
    else:
        # fisrst parent that is a rigth child or main root
        while root.parent is not None and root is root.parent.left:
            root = root.parent
        return root.parent


def succ_BST(root: Node) -> Node:
    if root.right is not None:
        # child on one right and max deep left
        root = root.right
        while root.left is not None:
            root = root.left
        return root
    else:
        # first parent that that is a left child or main root
        while root.parent is not None and root is root.parent.right:
            root = root.parent
        return root.parent


def sol(root: Node, T: list) -> int:
    s = 0
    for node in T:
        prev = prev_BST(node)
        succ = succ_BST(node)
        if prev is not None and succ is not None and prev.key + succ.key == node.key * 2:
            s += node.key

    return s


runtests(sol, all_tests=True)

w11 = Node(11, None)
w5 = Node(5, w11)
w11.left = w5
w15 = Node(15, w11)
w11.right = w15
w3 = Node(3, w5)
w5.left = w3
w8 = Node(8, w5)
w5.right = w8
w12 = Node(12, w15)
w15.left = w12
w7 = Node(7, w8)
w8.left = w7
w10 = Node(10, w8)
w8.right = w10
T = [w5, w7, w8, w11, w12]

print(sol(w11, T))
