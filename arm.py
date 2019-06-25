no= int(input())  
so = 0  
temp = no  
  
while temp > 0:  
   digit = temp % 10  
   so += digit ** 3  
   temp //= 10  
  
if no == so:  
   print("yes")  
else:  
   print("no")  
