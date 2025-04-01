#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

#Ask user for input
#Ask user for keyword/s to find
#Initialize counter to track occurrence
#loop through input
#Print result

text = input("Enter text")
keyword = input("Keyword to count: ")

for i in range(len(text) - len(keyword) + 1):
    if text[i:i + len(keyword)] == keyword:
        count += 1
print(f"{count} times appeared")
