#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
#Ask user to input a text
#Ask user to input the total width
#Set space equal to width
#Create loop that adds spaces to text until it's equal with the entered width
#Print the final output

text = input("Enter text: ")
width = int(input("Enter width: "))
space = width

while len(text) < width:
    text = text + " "
print(f'"{text}"')