def loop_size(node):
    slow = node.next
    fast = node.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    fast = fast.next
    count = 1

    while slow != fast:
        fast = fast.next
        count += 1

    return count
