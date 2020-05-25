class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head: Node) -> Node:
    # initialize variables
    current_node = head
    prev_node = next_node = None

    # while there are still nodes
    while current_node is not None:
        # save the node to visit next
        next_node = current_node.nextnode

        # replace next node with the previous one
        current_node.nextnode = prev_node

        # update the previous node as the current one
        prev_node = current_node
        current_node = next_node

    return prev_node
