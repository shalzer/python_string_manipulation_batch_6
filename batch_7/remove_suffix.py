#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

#Ask user to input text
#ask user what suffix to remove
#Check if the input ends w entered suffix
#remove if yes
#print result

user_input = input("Enter text: ")
suffix = input("suffix to remove: ")

if user_input.endswith(suffix):
    user_input = user_input[:-len(suffix)]
print(user_input)