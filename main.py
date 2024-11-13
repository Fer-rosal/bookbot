def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_wordcount = get_book_wordcount(text)
    print(f"---- Begin report of {book_path} ----")
    print(f" Words found in document: {text_wordcount}")
    characters_dictionary = character_count(text)
    chars_sorted_list = character_sort_filter(characters_dictionary)
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

def character_sort_filter(char_dictionary):
    character_list = []
    for char in char_dictionary:
        character_list.append({"char":char,"count":char_dictionary[char]})
    character_list.sort(reverse=True, key=sort_on)
    return(character_list)

def sort_on(dict):
    return dict["count"]    

def get_book_wordcount(text):
    text_length=len(text.split())
    return text_length

def get_book_text(path):
    with open(path) as f:
        return f.read()


def character_count(text):
    chars = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in chars:
            chars[c]+= 1
        else:
            chars[c] = 1
    return chars

main()