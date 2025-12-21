import sys
from stats import count_words, count_characters, sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_book):
    with open(path_to_book) as book:
        return book.read()

def main():
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    characters_dict = count_characters(book)
    characters_sorted = sort_characters(characters_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in characters_sorted:
        if char_dict["char"].isalpha():
            print(f'{char_dict["char"]}: {char_dict["num"]}')
    print("============= END ===============")

main()