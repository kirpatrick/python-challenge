from collections import Counter
import statistics

# Store the file paths associated with the files
# file = './raw_data/paragraph_1.txt'
# file = './raw_data/paragraph_2.txt'
file = './raw_data/paragraph_3.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # This stores a reference to a file stream
    # print(text)

    # Store all of the text inside a variable called "lines"
    # lines = text.read()

    # Print the contents of the text file
    # print(lines)
    wordCount = Counter(text.read().split())
    sentenceCount = Counter(text.read().split("."))

# print(wordcount)

# Print Results to terminal
print("Paragraph Analysis")
print("---------------------------------")
# Assess the passage for each of the following:

# Approximate word count
print(f"Approximate Word Count:  {sum(wordCount.values())}")
#################################################################################

# Approximate sentence count
print(f"Approximate Sentence Count:  {sum(sentenceCount.values())}")
#################################################################################

# Approximate letter count (per word)
print(statistics.mean(text.values()))
#################################################################################

# Average sentence length (in words)

#################################################################################

