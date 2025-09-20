from stats import word_count, character_count, sort_char_dict
import sys
if len(sys.argv) > 1:
    path = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_text = get_book_text(path)
    count = word_count(book_text)
    x = character_count(book_text)
    sorted = sort_char_dict(x)
    print_report(path, count, sorted)
    sys.exit(0)
    

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:
    main()