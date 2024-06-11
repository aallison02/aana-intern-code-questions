# Question 6
# Python-Specific Questions:
# Question: Implement a Python function that takes a string and returns a dictionary where the keys are the unique words in the string, and the values are the frequencies of each word.

# Code solution here

def word_frequencies(text):
    
    # Returns a dictionary where the keys are unique words in the input string and the values are the frequencies of each word.
    # :param text: Input string
    # :return: Dictionary with word frequencies
    
    # Remove punctuation and convert to lowercase
    text = ''.join(char.lower() if char.isalnum() else ' ' for char in text)
    words = text.split()
    
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

# Example usage
input_text = "One fish, two fish, red fish, blue fish."
frequencies = word_frequencies(input_text)
print(frequencies)  # Output: {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
