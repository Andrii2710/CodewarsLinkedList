class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise ValueError

    current = node
    for i in range(index):
        current = current.next
        if current is None:
            raise ValueError

    return current
