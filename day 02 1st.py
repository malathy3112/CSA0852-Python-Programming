l=[]
a=int(input("Enter number of elements:"))
for i in range(0,a):
    ele=int(input("Enter the value:"))
    l.append(ele)
print(l)
m=int(input("\nwhich largest element do you want to find?"))
l.sort(reverse=True)
if(m==1):
    print("\nyour",m,"st largest element is:",l[0])
elif(m==2):
    print("\nyour",m,"nd largest element is:",l[1])
elif(m==3):
    print("\nyour",m,"rd largest element is:",l[2])
else:
    print("\nyour",m,"th largest element is:",l[m-1])

n=int(input("\nwhich smallest element do you want to find?"))
l.sort(reverse=False)
if(n==1):
    print("\nyour",n,"st smallest element is:",l[0])
elif(n==2):
    print("\nyour",n,"nd smallest element is:",l[1])
elif(n==3):
    print("\nyour",n,"rd smallest element is:",l[2])
else:
    print("\nyour",n,"th smallest element is:",l[n-1])

print("The sum of",l[m],"and",l[n],"is:",l[m]+l[n])
print("The difference of",l[m],"and",l[n],"is:",l[m]-l[n])
