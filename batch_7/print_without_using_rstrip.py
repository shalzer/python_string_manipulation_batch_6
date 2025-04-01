#Ask user for input
#Start from last character of the string
#Loop backwards
#Trim the spaces of the string
#Print the trimmed string

user_input = input("Enter text: ")
last_entered = len(user_input) - 1

while last_entered >= 0 and user_input[last_entered] == ' ':
    last_entered -= 1