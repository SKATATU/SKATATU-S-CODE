num=[12,34,56,23,12,4]
bound = 34
count = 0
sum=0
for i in range (0, len(num)):
  if num[i] < bound:
    count += 1 
    sum += num[i]
print("The sum of numbers lower than 34 is:", sum, "and the count is:", count)

