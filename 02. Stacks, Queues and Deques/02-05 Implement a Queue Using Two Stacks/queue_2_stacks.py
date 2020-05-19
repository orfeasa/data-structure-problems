from typing import Any


class Queue2Stacks(object):
    def __init__(self) -> None:
        self.inbox = []
        self.outbox = []

    # we will use stack 1 to enqueue items (push), and stack 2 to dequeue items (pop)
    # pushing all the items in a stack and then popping them all reverses their order,
    # so before any operation we need to move all the items to the respective stack

    def enqueue(self, element: Any) -> None:
        # move all elements to stack 1
        while len(self.outbox) != 0:
            self.inbox.append(self.outbox.pop())

        self.inbox.append(element)

    def dequeue(self) -> Any:
        # move all elements to stack 2
        while len(self.inbox) != 0:
            self.outbox.append(self.inbox.pop())

        return self.outbox.pop()
