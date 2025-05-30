def get_num_words(book_text: str):
    words = book_text.split()
    return len(words)

def get_chars_dict(book_text: str):
    character_count = {}
    lower_case_text = book_text.lower()
    for c in lower_case_text:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count