class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# hash table (set) approach
def cycle_check(node: Node) -> bool:
    # initialize set of accessed nodes
    nodes_accessed = set()
    current_node: Node = node

    while current_node is not None:
        if current_node in nodes_accessed:
            return True
        else:
            nodes_accessed.add(current_node)
        current_node = current_node.nextnode

    return False


# Two pointers approach (space complexity O(1))
# In this approach, we have 2 pointers. If the list is a cycle, in each step,
# the distance between the 2 pointers is reduced by 1. If not, the fast pointer
# will reach the end (None)
def cycle_check2(node: Node) -> bool:
    if node is None or node.nextnode is None:
        return False

    # initialize 2 pointers
    slow: Node = node
    fast: Node = node.nextnode

    while slow != fast:
        if fast is None or fast.nextnode is None:
            return False
        slow = slow.nextnode
        fast = fast.nextnode.nextnode

    return True
