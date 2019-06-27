s=int(input("enter the num:"))
if s>1:
    for h in range(2,s):
        if(s%h)==0:
            print(s,"is a prime number")
            print(h,"times",s//i,"is",num)
            break
        else:
            print(s,"is prime number")
else:
    print(s,"is not a prime number")
