from stats import word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

    
def main():
    path = 'books/frankenstein.txt'
    book_text = get_book_text(path)
    #word_count(book_text)
    character_count(book_text)
    

main()