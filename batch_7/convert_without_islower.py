#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

#Ask user to enter anything
#Using .upper, convert the input into upper case
#Then using .swapcase, it converts the input into lower case
# Print the result

text = input("Enter text: ")
TEXT = text.upper()
text_lowercase = TEXT.swapcase()
print(text_lowercase)