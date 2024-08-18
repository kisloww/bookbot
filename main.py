def main():
    path = "books/frankenstein.txt"
    file_content = get_book_text(path)

    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_content)} words found in the document\n")

    char_list = chars_dict_to_sorted_list(count_characters(file_content))
        
    for element in char_list:
        if element["char"].isalpha():
            print(f"The {element['char']} character was found {element['number']} times")
    print("--- End report ---")
            
def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char in char_dict:
        number = char_dict[char]
        char_list.append({"char":char, "number":number})
    char_list.sort(reverse=True, key=sort_dict)
    return char_list

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    characters = {}
    for character in lower_text:
        if character not in characters:
             characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_dict(dict):
    return dict["number"]
    
def get_book_text(path):
     with open(path) as f:
        return f.read()

main()