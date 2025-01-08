import string

def create_file():
    user_input = input("Write an paragraph to create sample file: ")
    with open("sample.txt", "w") as f:
        f.write(user_input)

def read_file(filename):
    try: 
        with open(filename, "r") as f:
            text = f.read()
        return text
    except FileNotFoundError:
        create_file()
        with open(filename, "r") as f:
            content = f.read()
        return content

def clean_text(text):
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    words = text.split()
    return words

def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def top_words(frequency, n):
    top_5 = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:n]
    return top_5

def report(total_words, top_words):
    with open("word_count_report.txt", "w") as f:
        f.write("Total number of words: {total_words}\n")
        f.write("5 most common words:\n")
        for word, count in top_words:
            f.write(f"{word}: {count}\n")

def main():
    filename = "sample.txt"
    text = read_file(filename)
    words = clean_text(text)
    if not words:
        print('File is empty')
        return
    frequency = count_word_frequency(words)
    total_words = len(words)
    top_n_words = top_words(frequency, 5)

    print(f"Total number of words: {total_words}")
    print("Top words:")
    for word, count in top_n_words:
        print(f"{word} - {count}")
    report(total_words, top_n_words)

if __name__ == "__main__":
    main()