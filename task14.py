def count_word_frequency(paragraph):
    words = paragraph.split()  # Split paragraph into words
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1  # Count each word

    for word, count in word_count.items():
        print(f"{word}: {count}")

# Example usage
paragraph = "apple banana apple orange banana banana"
count_word_frequency(paragraph)
