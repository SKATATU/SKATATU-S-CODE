booth = [[]]
for i in range(1,6):
  for j in range(1,6):
    booth[i,j] = ""


# create a 2D array with 6 rows and 6 columns
arr = [[0 for j in range(6)] for i in range(6)]

# fill the array with the numbers in the specified format
for i in range(6):
    if i % 2 == 0:
        for j in range(6):
            arr[i][j] = i*6 + j + 1
    else:
        for j in range(6):
            arr[i][j] = (i+1)*6 - j - 1

# print the array
for i in range(6):
    for j in range(6):
        print(arr[i][j], end='\t')
    print()
    

a=int(input("Please input the 1st side length"))
b=int(input("Please input the 2nd side length"))
c=int(input("Please input the 3rd side length"))
if a <= 0 or b <= 0 or c <= 0:
  print("Cannot form a triangle")
elif (a+b<=c) or (a+c<=b) or (c+b<=a):
  print("Cannot form a triangle")
else:
  print("This is a/an ", end="")
  if a==b and b==c:
    print("equilateral triangle")
  elif a==b or b==c or a==c:
    print("Isoceles triangle")
  else:
    print("Scalene triangle")