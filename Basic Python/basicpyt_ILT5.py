#LAB 5
import numpy as np
#Q1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
file=open("lab5.txt",'r')
for i in file:    
    print(i)
file.close()

#Q2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
file=open('ABC.txt','w')
file.write("hello everyone")
file.close()

file=open('ABC.txt','r')
t =file.read()
r=t.split()
print(len(r))
file.close()

#Q3. Write a function in Python to count uppercase character in a text file “ABC.txt”
file = open('ABC.txt', 'r')
t = file.read()
words = t.split()
uppercase_words = []

for word in words:
    uppercase_word = word.upper()
    uppercase_words.append(uppercase_word)

print("Uppercase words:", ' '.join(uppercase_words))
file.close()

#Q4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
file=open('story.txt','w')
file.write("this is a short story of any python program. it is bery nice and short.tou may read it")
file.close()
file=open("story.txt",'r')
def display_words(file_name):
    short_words=[]
    for line in file:
        words = line.split()
        for word in words:
            if len(word) < 4:
                short_words.append(word)
        print(' '.join(short_words))

display_words('story.txt')
file.close()

#Q1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
a = int(input("enter the first no."))
b = int(input("enter the second no."))
try:
    print(a/b)
    print("inside the try block")
except ZeroDivisionError as e:
    print("zero error")


#Q2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    a = int(input("enter the no."))
    print(a)
except ValueError:
    print("Invalid Integer")

#Q3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    file=open('myfile.txt','r')
except:
    print("no file")

#Q4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
try:
    a = int(input("enter the first no."))
    b = int(input("enter the second no."))
except ValueError:
    print("Invalid Integer")
