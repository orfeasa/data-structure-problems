# Find the Missing Element

## Problem

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

```python
>>> finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
5
```

5 is the missing number

## Code

Create your solution in the form:

```python
def finder(arr1: List, arr2: List) -> int:
    pass
```

## Examples

```python
>>> arr1 = [1,2,3,4,5,6,7]
>>> arr2 = [3,7,2,1,4,6]
>>> finder(arr1,arr2)
5
```

```python
>>> arr1 = [5,5,7,7]
>>> arr2 = [5,7,7]
>>> finder(arr1,arr2)
5
```
