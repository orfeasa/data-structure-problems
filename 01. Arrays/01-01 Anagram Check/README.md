# Anagram Check

## Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

    "public relations" is an anagram of "crap built on lies."

    "clint eastwood" is an anagram of "old west action"

**Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**

Leetcode: Valid Anagram (https://leetcode.com/problems/valid-anagram/description/)

## Code

Create your solution in the form:

```python
def anagram(s1: str, s2: str) -> bool:
    pass
```

## Examples

```python
>>> anagram('dog','god')
True
>>> anagram('clint eastwood','old west action')
True
>>> anagram('aa','bb')
False
```
