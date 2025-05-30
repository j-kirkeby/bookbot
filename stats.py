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

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(dictionary: dict):
    char_stats = []

    for char in dictionary:
        stat = {}
        stat["char"] = char
        stat["num"] = dictionary[char]
        char_stats.append(stat)

    char_stats.sort(reverse=True, key=sort_on)

    return char_stats

