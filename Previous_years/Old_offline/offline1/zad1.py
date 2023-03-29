from zad1testy import Node, runtests


def SortH(p: Node, k: int) -> Node:
    # add guardian
    head = Node()
    head.next = p

    prev = head

    while prev.next.next is not None:
        i = 0
        ind = prev.next
        check = ind.val
        while i < k and ind.next is not None:
            if ind.next.val < check:
                check = ind.next.val
                q = ind
                a = ind.next
            ind = ind.next
            i += 1
        if check != prev.next.val:
            q.next = q.next.next
            a.next = prev.next
            prev.next = a

        prev = prev.next

    return head.next


runtests(SortH)
