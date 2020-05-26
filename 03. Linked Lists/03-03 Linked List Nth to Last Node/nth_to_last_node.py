from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n: int, head: Node) -> Optional[Node]:
    current_node = head

    # advance N positions. If the list is shorter than that return None
    for _ in range(n):
        if current_node.nextnode is None:
            return None
        current_node = current_node.nextnode

    # Now advance both the current and the Nth to last nodes by one, until the end is reached
    nth_to_last_node = head
    while current_node is not None:
        nth_to_last_node = nth_to_last_node.nextnode
        current_node = current_node.nextnode

    return nth_to_last_node
