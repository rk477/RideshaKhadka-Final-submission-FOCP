# 4. One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the different symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
# Hint: There are many ways to do this. It is obviously a dictionary, but we will want
# zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
# best to ignore that initially, and then check the usual resources for the runes


from collections import Counter

def analyze_frequency(message):
    # Convert the message to lowercase and remove non-alphabetic characters
    cleaned_message = ''.join(ch for ch in message.lower() if ch.isalpha())
    
    # use built-in Counter function to count the frequency of each letter
    letter_frequency = Counter(cleaned_message)
    
    # Sort the dictionary by value in descending order and get the six most common letters
    most_common_letters = letter_frequency.most_common(6)
    
    # Print the six most common letters and their counts
    for letter, count in most_common_letters:
        print(f"Letter: '{letter}', Count: {count}")

# function call with a test message
test_message = "This is a test message. It shows the 6 most common letters and their counts."
analyze_frequency(test_message)
