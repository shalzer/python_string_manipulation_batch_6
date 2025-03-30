# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

#Ask user to enter a text
#Ask for width
#check if text is equal or greater than the width
#if yes, keep the text
#else, calculate the number of spaces needed to add to total width
#print output

text = input("Enter text: ")
width = int(input("Enter total width: "))
if len(text) >+ width:
    result = text
else:
    total_space = width - len(text)
    left_space = total_space // 2
    right_space = total_space - left_space
    result = " " * left_space + text + " " * right_space
print(result)