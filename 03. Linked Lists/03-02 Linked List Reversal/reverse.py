class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(head: Node) -> Node:
    # initialize variables
    current_node = next_node = head
    prev_node = None

    # while there are still nodes
    while next_node is not None:
        # set as current node the one that was after the previous one
        current_node = next_node

        # save the node to visit next
        next_node = current_node.nextnode

        # replace next node with the previous one
        current_node.nextnode = prev_node

        # update the previous node as the current one
        prev_node = current_node

    return current_node
