# Implement a Queue - Using Two Stacks

## Problem

Given the Stack class below, implement a Queue class using **two** stacks! Use a Python list data structure as your Stack.

```python
# Uses lists instead of your own Stack class.
stack1 = []
stack2 = []
```

## Code

```python
class Queue2Stacks(object):
    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # FILL OUT CODE HERE
        pass

    def dequeue(self):
        # FILL OUT CODE HERE
        pass
```

## Examples

```python
>>> q = Queue2Stacks()
>>> for i in range(5):
...     q.enqueue(i)
...
>>> for i in range(5):
...     print(q.dequeue())
...
0
1
2
3
4
```
