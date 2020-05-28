from typing import List


def word_split(phrase: str, list_of_words: List, output: List = []) -> List:
    # Check for each word in the list if it fits the beginning of the phrase
    for word in list_of_words:
        if phrase[:len(word)] == word:
            if len(phrase) > len(word):
                return word_split(phrase[len(word):], list_of_words, output + [word])
            else:
                return output + [word]

    return []
