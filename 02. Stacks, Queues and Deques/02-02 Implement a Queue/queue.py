from typing import Any, List


class Queue(object):
    def __init__(self) -> None:
        self.items: List[Any] = []

    def size(self) -> int:
        # Returns the size of the Queue
        return len(self.items)

    def is_empty(self) -> bool:
        # Checks if Queue is Empty
        return self.size() == 0

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        return self.items.pop(0)
