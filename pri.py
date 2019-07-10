init=10
end=50
for i in range(init,end+1):
    if i >1:
        for h in range(2,i):
            if(i%h)==0:
                break
            else:
                print(i)
