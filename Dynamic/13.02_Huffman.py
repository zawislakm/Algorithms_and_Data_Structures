class Huffman_Tree:

    def __init__(self, value: int, letter: str = None):
        self.value = value
        self.left = None
        self.right = None
        self.letter = letter


def huffman_code(L: list):
    tree_elements = []
    for letter, value in L:
        tree_elements.append(Huffman_Tree(value, letter))

    while len(tree_elements) > 1:
        tree_elements.sort(key=lambda x: x.value)
        first = tree_elements.pop(0)
        second = tree_elements.pop(0)
        new_node = Huffman_Tree(first.value + second.value)
        new_node.left = first
        new_node.right = second
        tree_elements.append(new_node)

    tree_node = tree_elements[0]
    message = []
    def get_letter(node, code, i=0):
        nonlocal message
        if node.letter is not None:
            message.append(node.letter)
            return
        if code[i] == "0":
            get_letter(node.left, code, i + 1)
        else:
            get_letter(node.right, code, i + 1)

    message_codes = ["000","01","000","01","10","11"]

    for code in message_codes:
        get_letter(tree_node, code)

    print(f'Found massage is {message}')


L = [("a", 50), ("b", 5), ("c", 60), ("d", 65), ("e", 20)]
huffman_code(L)
