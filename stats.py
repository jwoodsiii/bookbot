from collections import Counter


def word_count(text: str) -> int:
    return len(text.split())


def char_count(text: str) -> dict[str, int]:
    # O(n) time, O(k) space where k is unique chars
    # optimal solution for time and space
    out = dict()
    for char in text:
        char = char.lower()
        out[char] = 1 if out.get(char) is None else out[char] + 1
    return out

    # could also use a counter from collections
    # return dict(Counter(text.lower()))
    # O(n) time and O(n+k) space, counter has to create full lowercase copy of text


def beautify_dict(charCount: dict[str, int]) -> dict[str, int]:
    out = []
    for k, v in charCount.items():
        add = dict()
        add.update({"char": k, "num": v})
        out.append(add)

    def sort_on(items):
        return items["num"]

    out.sort(reverse=True, key=sort_on)

    return out
