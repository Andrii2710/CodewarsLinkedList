def linked_list_from_string(list_repr: str) -> Node | None:
    elements = list_repr.split(" -> ")

    values = elements[:-1]

    current_node = None

    for val in reversed(values):
        current_node = Node(int(val), current_node)

    return current_node
