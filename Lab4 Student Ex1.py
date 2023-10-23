text=input("Enter text: ")
length=int(len(text))
highest=length-1
final=""
for i in range(highest,-1,-1):
 final=final+(text[i])
if text==final:
 print("The text is a Palindrome")
else:
 print("Sorry")