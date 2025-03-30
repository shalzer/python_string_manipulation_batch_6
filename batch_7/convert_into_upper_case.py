#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

#Ask user to enter a text
#Using .lower, convert the input into lower case
#Then using .swapcase, it converts the input into upper case
# Print the result

text = input("Enter text: ")
TEXT = text.lower()
text_uppercase = TEXT.swapcase()
print(text_uppercase)