def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char = get_sorted_list(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for item in sorted_char:
        if item["char"].isalpha():
          print(f"the '{item['char']}' character was found {item['num']} times")
    
    print(f"\n--- End report ---")

def sort_on(d):
    return d["num"]

def get_sorted_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_word_count(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

main()