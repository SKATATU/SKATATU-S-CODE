num1 = int(input("Input the 1st number:"))
num2 = int(input("Input the 2nd number:"))

i = 1 
hcf = i

while i <= num1 and i <= num2:
  if num1 % i == 0 and num2 % i == 0:
    hcf = i
  i+= 1  
print("The largest common factor of these two numbers are:", hcf)
