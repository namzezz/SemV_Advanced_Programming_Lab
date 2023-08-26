def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create an empty dictionary to store word counts
    word_counts = {}
    
    # Iterate through each word
    for word in words:
        # Remove any punctuation marks from the word
        word = word.strip('.,!?;:()[]{}"\'')
        
        # Convert the word to lowercase to handle case-insensitivity
        word = word.lower()
        
        # If the word is not empty, update the dictionary
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    return word_counts

# Get input from the user
sentence = input("Enter a sentence: ")

# Count the words using the function
word_counts = count_words(sentence)

# Print the word counts
for word, count in word_counts.items():
    print(f"'{word}': {count}")

# Calculate and print the sum of word counts
total_words = sum(word_counts.values())
print("Total words:", total_words)
