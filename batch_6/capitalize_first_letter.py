#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

#Ask for user's input
#convert the first letter to uppercase, the rest to lowercase
#print result

text = input("Enter text: ")
result = text[0].upper() + text[1:].lower()
print(result)