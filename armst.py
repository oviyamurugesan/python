f,g=map(int,input().split())
for h in range (f+1,g):
    a=0
    n=h
    while(n>0):
        b=n%10
        n=n//10
        c=b**3
        a=a+c
    if(h==a):
        print(a,end=' ')
