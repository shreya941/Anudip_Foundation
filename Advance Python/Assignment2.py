# Writing content to the file
file = open("Indias.txt", 'w', encoding='utf-8')
file.write("Hello, this is a india india india india sample file. Hello again. Just saying hello one more time.")
file.close()

# Reading the file and counting occurrences of "hello"
file = open("Indias.txt", 'r', encoding='utf-8')
contents = file.read().lower()  # Read the file and convert to lower case to handle case sensitivity
file.close()  # Close the file after reading

words = contents.split()  # Split the contents into words
word_count = words.count('india')  # Count the occurrences of the word "hello"

# Print the result
print(f"The word 'india' occurs {word_count} times in the file.")

#ques 2---------------------------------------------------------------------------------------------------------
# Open the file in read mode
file = open("story.txt", 'w', encoding='utf-8')
file.write("this is my world.\n t se i dont know.\n hellooow.\nt is good. \nt for teddy. \nwowwwwww")
file.close()
file = open("story.txt", 'r', encoding='utf-8')

# Initialize a counter for lines starting with 't'
count = 0

# Read the file line by line
for line in file:
    if line.lower().startswith('t'):
        print(line.strip())  # Print the line (strip to remove extra whitespace)
        count += 1

# Close the file
file.close()

# Print the count of lines starting with 't'
print(f"Number of lines starting with 't': {count}")

#q3-----------------------------------------------------------------------------------------------------------------
file = open("hello.txt", 'w', encoding='utf-8')
file.write("helolo worlds my name is shreyaaaaaa")
# Define the vowels
vowels = 'aeiou'

# Initialize counters for vowels and consonants
vowel_count = 0
consonant_count = 0

# Open the file in read mode
file = open("hello.txt", 'r', encoding='utf-8')

# Read the file contents
contents = file.read().lower()  # Convert to lower case to handle case insensitivity

# Close the file
file.close()

# Iterate through each character in the file contents
for char in contents:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the counts
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
