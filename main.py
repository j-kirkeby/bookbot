from stats import get_num_words, get_chars_dict

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()