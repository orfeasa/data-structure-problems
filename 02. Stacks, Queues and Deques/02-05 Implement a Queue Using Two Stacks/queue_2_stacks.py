from typing import Any, List


class Queue2Stacks(object):
    def __init__(self) -> None:
        self.inbox: List[Any] = []
        self.outbox: List[Any] = []

    def enqueue(self, element: Any) -> None:
        # push new element onto inbox
        self.inbox.append(element)

    def dequeue(self) -> Any:
        # If outbox is empty, refill it by popping each element from inbox and
        # pushing it onto outbox. Pop and return the top element from outbox
        if len(self.outbox) == 0:
            while len(self.inbox) != 0:
                self.outbox.append(self.inbox.pop())

        return self.outbox.pop()
