def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_content = f.read()
    # print(count_words(file_content))
    result = count_characters(file_content)
    print(result)

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


main()