# String Compression

## Problem

Given a string in the form `'AAAABBBBCCCCCDDEEEE'` compress it to become `'A4B4C5D2E4'`. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for `'AAB'` to return `'A2B1'` even though this technically takes more space.

The function should also be case sensitive, so that a string `'AAAaaa'` returns `'A3a3'`.

## Code

Create your solution in the form:

```python
def compress(s: str) -> str:
    pass
```

## Example

```python
>>> compress('AAAAABBBBCCCC')
'A5B4C4'
```
