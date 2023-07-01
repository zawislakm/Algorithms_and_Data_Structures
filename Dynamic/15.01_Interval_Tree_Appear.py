# appearing of intervals on given point
class IntervalTree:
    def __init__(self, value: int = None, left=None, right=None, parent=None, span=None):

        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.intervals = []
        if span is None:
            span = [-1 * float('inf'), float('inf')]
        self.span = span

    def in_span(self, given_interval: list) -> bool:
        if self.span[0] >= given_interval[0] and self.span[1] <= given_interval[1]:
            return True
        return False

    def common_part(self, given_interval: list) -> bool:
        if given_interval[1] < self.span[0] or given_interval[0] > self.span[1]:
            return False
        return True


def build_tree(intervals: list) -> IntervalTree:
    points = []

    for u, v in intervals:
        if u not in points:
            points.append(u)
        if v not in points:
            points.append(v)

    points.sort(key=lambda x: x)
    print(points)

    def middle_element(i=0, j=len(points) - 1) -> int:
        return (i + j) // 2

    def make_tree(prev_node: IntervalTree = None, left_end: int = 0, right_end: int = len(points) - 1,
                  left_span_end: int = -1 * float('inf'), right_span_end: int = float('inf'),
                  last: bool = False) -> IntervalTree:

        if last is True:
            node = IntervalTree()
            node.parent = prev_node
            node.span = [left_span_end, right_span_end]
            return node

        mid_elem = middle_element(left_end, right_end)
        node = IntervalTree()
        node.parent = prev_node
        node.value = points[mid_elem]
        node.span = [left_span_end, right_span_end]

        if left_end == right_end:
            last = True

        node.left = make_tree(node, left_end, mid_elem - 1, left_span_end, points[mid_elem], last)
        node.right = make_tree(node, mid_elem + 1, right_end, points[mid_elem], right_span_end, last)
        return node

    root = make_tree()

    return root


def print_tree(node: IntervalTree):
    if node.left is not None:
        print_tree(node.left)
    print(f"Node value is: {node.value}, node span is: {node.span}, and found intervals are: {node.intervals}")
    if node.right is not None:
        print_tree(node.right)


def solve_task(root: IntervalTree, given_intervals: list) -> None:
    def put_interval(node: IntervalTree, interval: list):
        if node.in_span(interval):
            node.intervals.append(interval)
            return

        if node.left is not None:
            if node.left.common_part(interval):
                put_interval(node.left, interval)
        if node.right is not None:
            if node.right.common_part(interval):
                put_interval(node.right, interval)

    for interval in given_intervals:
        put_interval(root, interval)

    print_tree(root)


def check_intervals_point(root: IntervalTree, value: int) -> int:
    print("Solution:")
    in_intervals = []

    def go_down(node: IntervalTree):
        nonlocal in_intervals

        for interval in node.intervals:
            if interval not in in_intervals:
                in_intervals.append(interval)

        print(f"Node value: {node.value}, node intervals: {node.intervals}")
        if node.left is not None and node.value >= value:
            go_down(node.left)
        if node.right is not None and node.value <= value:
            go_down(node.right)

    go_down(root)

    return len(in_intervals)


given_intervals = [[0, 10], [5, 20], [7, 12], [10, 15]]
tree_root = build_tree(given_intervals)
solve_task(tree_root, given_intervals)
print(check_intervals_point(tree_root, 13))
