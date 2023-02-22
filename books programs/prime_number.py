num = int(input("Please input a number:"))
if num > 1:
  isPrime = True
else:
  isPrime = False
  
for i in range (2,num//2):
  if(num%1 == 0):
    isPrime = False
    
if isPrime == True:
  print(num, "is a prime number.")
else: 
  print(num, "is NOT a prime number.")
