#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#Ask user's input
#Check if it starts w prefix
#remove if yes
#print result

user_input = input("Enter text: ")
prefix = input("Prefix to remove: ")

if user_input.startswith(prefix):
    user_input = user_input[len(prefix):]