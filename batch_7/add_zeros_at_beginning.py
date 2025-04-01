# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

#Ask user for input
#Ask user for width
#Add zeros if width entered is shorter than the string
#Print result

text = input("Enter text: ")
width = int(input("Enter width: "))

if len(text) < width:
    text = "0" * (width - len(text)) + text