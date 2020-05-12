def rev_word(s: str) -> str:
    words = s.strip().split()
    return " ".join(words[::-1])
