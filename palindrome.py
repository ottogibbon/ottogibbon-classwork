myString = input (“ Please enter a word or phrase to be tested: ”)
stack = []
for _ in myString:
    stack.append(c)
newString = ""
for _ in range(len(stack)):
    newString = newString + stack.pop()

if myString == newString:
    print("Palindrome")
else:
    print( " not palindrome ")
