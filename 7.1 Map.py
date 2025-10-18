sentence = "I am Syed Hanzala Alam" # Stores a sentence in a variable.
words = sentence.split() # Splits the sentence into separate words.
print(words)
lengths = map(lambda word: len(word), words) # Uses a lambda function to find the length of each word.
list(lengths) # Turns those lengths into a list.