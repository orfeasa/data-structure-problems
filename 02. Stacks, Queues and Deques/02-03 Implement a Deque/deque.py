from typing import Any, List


class Deque(object):
    def __init__(self) -> None:
        self.items: List[Any] = []

    def size(self) -> int:
        # Checks the Size
        return len(self.items)

    def is_empty(self) -> bool:
        # Checks if its empty
        return self.size() == 0

    def add_front(self, element) -> None:
        self.items.insert(0, element)

    def add_rear(self, element) -> None:
        self.items.append(element)

    def remove_front(self) -> Any:
        return self.items.pop(0)

    def remove_rear(self) -> Any:
        return self.items.pop()
