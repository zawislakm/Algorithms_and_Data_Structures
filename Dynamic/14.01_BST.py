class BSTnode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key
        self.data = None

    # search
    # min/max
    # prev/succ
    # insert
    # remove


def print_BST(root: BSTnode):
    if root.left is not None:
        print_BST(root.left)
    print(root.key)
    if root.right is not None:
        print_BST(root.right)


def search_BST(root: BSTnode, key: int) -> BSTnode:
    while root is not None:
        if root.key == key:
            return root
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root  # means None


def min_BST(root: BSTnode) -> BSTnode:
    while root.left is not None:
        root = root.left
    return root


def max_BST(root: BSTnode) -> BSTnode:
    while root.right is not None:
        root = root.right
    return root


def succ_BST(root: BSTnode) -> BSTnode:
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


def prev_BST(root: BSTnode) -> BSTnode:
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


def insert_BST(root: BSTnode, new_node: BSTnode) -> bool:
    if root.key == new_node.key:
        # already in BST
        return False

    if root.key < new_node.key:
        if root.right is None:
            root.right = new_node
            new_node.parent = root
            return True
        else:
            insert_BST(root.right, new_node)
    else:
        if root.left is None:
            root.left = new_node
            new_node.parent = root
            return True
        else:
            insert_BST(root.left, new_node)

    return False


def remove_BST(root: BSTnode, removed_key: int) -> BSTnode:
    """
    Removes a node with the specified key from the Binary Search Tree (BST).

    :param root: The root node of the BST.
    :param removed_key: The key of the node to be removed.
    :return: The removed node from BST

    3 cases:
    1. Node to remove has 0 children
    2. Node to remove has 1 child
    3. Node to remove has 2 children
    """


    removed_node = search_BST(root, removed_key)

    if removed_node.left is None and removed_node.right is None:
        # Case 1. Simple removing pointers to removed node
        parent_removed_node = removed_node.parent

        if removed_node is parent_removed_node.left:
            parent_removed_node.left = None
        elif removed_node is parent_removed_node.right:
            parent_removed_node.right = None

        removed_node.parent = None

        return removed_node

    if removed_node.left is None or removed_node.right is None:
        # Case 2. Changing pointer from parent of removed node to child of removed node
        parent_removed_node = removed_node.parent

        if removed_node.left is not None:
            child = removed_node.left
        else:
            child = removed_node.right

        if removed_node is parent_removed_node.left:
            parent_removed_node.left = child
        elif removed_node is parent_removed_node.right:
            parent_removed_node.right = child

        child.parent = parent_removed_node

        removed_node.parent = None
        removed_node.left = None
        removed_node.right = None
        return removed_node

    # Case 3. In place of removed node should be inserted successor of removed node

    successor_removed_node = succ_BST(removed_node)
    successor_removed_node = remove_BST(root, successor_removed_node.key)

    if removed_node.parent is not None:
        parent_removed_node = removed_node.parent
        if removed_node is parent_removed_node.left:
            parent_removed_node.left = successor_removed_node
        elif removed_node is parent_removed_node.right:
            parent_removed_node.right = successor_removed_node

        successor_removed_node.parent = parent_removed_node

    successor_removed_node.left = removed_node.left
    successor_removed_node.right = removed_node.right

    removed_node.left = None
    removed_node.right = None
    removed_node.parent = None

    return removed_node


# następnik węzła który ma dwojke dzieci ma najwyzej jedno dziecko, wazne przy usuwaniu

# oblicznie następnika i poprzednika w bst

# BST.png
bst20 = BSTnode(20)
bst17 = BSTnode(17, bst20)
bst30 = BSTnode(30, bst20)
bst20.left = bst17
bst20.right = bst30
bst5 = BSTnode(5, bst17)
bst19 = BSTnode(19, bst17)
bst17.left = bst5
bst17.right = bst19
bst18 = BSTnode(18, bst19)
bst19.left = bst18
bst27 = BSTnode(27, bst30)
bst35 = BSTnode(35, bst30)
bst30.left = bst27
bst30.right = bst35
bst40 = BSTnode(40, bst35)
bst35.right = bst40
bst50 = BSTnode(50, bst40)
bst40.right = bst50
bst100 = BSTnode(100, bst50)
bst50.right = bst100

remove_BST(bst20, 17)
print_BST(bst20)
