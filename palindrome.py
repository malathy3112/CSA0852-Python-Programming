n=int(input("Enter a number:"))
temp=n
reverse=0
while(n>0):
    digital=n%10
    reverse=reverse*10+digital
    n=n//10
if(temp==reverse):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
