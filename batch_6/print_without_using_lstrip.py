#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

#Ask the user to enter anything with spaces at beginning
#Remove the space at the beginning using strip
#Print the result

any = input("Enter anything with spaces at the beginning: ")
ANY = any.strip()
print(ANY)