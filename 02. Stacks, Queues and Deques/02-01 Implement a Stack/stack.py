from typing import Any, List


class Stack(object):
    def __init__(self) -> None:
        self.items: List[Any] = []

    def push(self, item: Any) -> None:
        # Push a new item
        self.items.append(item)

    def pop(self) -> Any:
        # Pop an item
        return self.items.pop()

    def peek(self) -> Any:
        # Peek at the top item
        if self.is_empty():
            raise Exception("Stack empty!")
        return self.items[-1]

    def size(self) -> int:
        # Return the size
        return len(self.items)

    def is_empty(self) -> bool:
        # Checks if its empty
        return self.size() == 0
