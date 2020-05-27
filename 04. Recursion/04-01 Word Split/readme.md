# Word Split

## Problem

Create a function called `word_split()` which takes in a string **phrase** and a set **list_of_words**. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

## Code

Create your solution in the form:

```python
def word_split(phrase, list_of_words, output = None):
    pass
```

## Examples

```python
>>> word_split('themanran',['the','ran','man'])
['the', 'man', 'ran']
>>> word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
['i', 'love', 'dogs', 'John']
>>> word_split('themanran',['clown','ran','man'])
[]
```
