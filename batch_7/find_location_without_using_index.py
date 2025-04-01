# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#Ask user for input
#Ask for keyword to find
#Check if keyword is in input
#Print the index if yes
from re import search

text = input("Enter text: ")
keyword = input("Enter keyword to find: ")
if keyword in text:
    print(text.find(keyword))