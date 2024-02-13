def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sorted_chars(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_chars:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item["letter"]}' character was found {item["count"]} times")
    print("--- End report ---")
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_chars(dict):
    key_list = []

    def sort_on(dict):
        return dict["count"]

    for key in dict:
        key_list.append({ "letter": key, "count": dict[key] })
    
    key_list.sort(reverse=True, key=sort_on)

    return key_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()