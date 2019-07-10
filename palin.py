h=int(input("enter the num:"))
temp=h
rev=0
while temp!=0:
    rev=(rev*10)+(temp%10)
    temp=temp//10
if h==rev:
    print("yes")
else:
    print("no")
