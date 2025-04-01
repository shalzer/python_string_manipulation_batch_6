#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

#Ask user for input
#Ask user for total width
#Add space at beginning to make it equal to entered width
#print result

text = input("Enter text: ")
width = int(input("Enter width: "))
text = " " * (width - len(text)) + text
print(f'"{text}')