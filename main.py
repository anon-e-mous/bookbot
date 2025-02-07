def get_text(text_path):
    with open(text_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for c in text:
        c = c.lower()
        if c in char_counts:
            char_counts[c] = char_counts[c] + 1
        else:
            char_counts[c] = 1
    return char_counts

def print_report(text_path, word_count, char_counts):
    print("--- Begin report of " + text_path + " ---")
    print(f"{word_count} words found in the document")
    print("")

    for item in char_counts:
        letter = item[0]
        if letter.isalpha():
            times = item[1]
            print(f"The \'{letter}\' character was found {times} times")
    print("--- End report ---")


def main():
    text_path = "books/frankenstein.txt"
    file_contents = get_text(text_path)
    word_count = count_words(file_contents)
    char_counts = count_chars(file_contents)
    char_counts_by_values = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    #print(char_counts)
    print_report(text_path, word_count, char_counts_by_values)

main()