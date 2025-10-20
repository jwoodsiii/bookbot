import sys
from stats import word_count, char_count, beautify_dict


def get_book_text(filePath: str) -> str:
    with open(filePath, "r") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    wc = word_count(book)
    cc = char_count(book)
    print(f"DEBUG: e count = {cc.get('e', 0)}")
    # print(cc)
    formatted = beautify_dict(cc)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in formatted:
        if item.get("char").isalpha():
            print(f"{item['char']}: {item['num']}")
        continue
    print("============= END ===============")


if __name__ == "__main__":
    main()
