#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

#Ask user to input text
#Ask user what prefix they would like to check
#Check if the input starts with the entered prefix
#Print if it starts with the entered prefix
#Else, it will print "does not start with"

text = input("Enter text: ")
prefix = input("Prefix to check: ")

if text[:len(prefix)] == prefix:
    print(f"The text starts with {prefix}")
else:
    print(f"The text does not start with {prefix}")