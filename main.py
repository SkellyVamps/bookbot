def character_count(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        char_count = character_count(file_contents)
        char_list = list(char_count.items())

        print("--- Begin report ---")
        print(f"{word_count} words found in the document\n")

        def alphabetical_sort(item):
            return item[0]

        char_list.sort(key=alphabetical_sort)
        
        for char, count in char_list:
            for c in char:
                if c.isalpha():
                    print(f"the '{char}' character was found {count} times")
        
        print("--- End Report ---")

main()