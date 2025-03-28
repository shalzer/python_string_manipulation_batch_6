#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

#Ask user to input a statement
#if the letter is in lowercase, convert into upper
#else, convert it to lowercase
#print the result

statement = input("Enter a statement: ")
result = ""

for letter in statement:
    if letter.islower():
        result += letter.upper()