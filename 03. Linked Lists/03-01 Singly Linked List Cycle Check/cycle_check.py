class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(node: Node) -> bool:
    # initialize set of accessed nodes
    nodes_accessed = {node}

    current_node: Node = node

    while current_node.nextnode is not None:
        current_node = current_node.nextnode
        if current_node in nodes_accessed:
            return True
        else:
            nodes_accessed.add(current_node)

    return False
