def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_content = f.read()
    print(count_words(file_content))


def count_words(text):
    words = text.split()
    return len(words)





main()