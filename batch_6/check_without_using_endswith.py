#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

#Ask user to input text
#Ask user what suffix they would like to check
#Check if the input ends with the entered suffix
#Print if it ends with the entered suffix
#Else, it will print "does not end with"

text = input("Enter text: ")
suffix = input("Suffix to check: ")

if text[-len(suffix):] == suffix:
    print(f"The text ends with {suffix}")