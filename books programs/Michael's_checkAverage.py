mark = [78,89,87,95,60,44,51,98,77,69]
def average():
  sum = 0
  for i in range(0, len(mark)):
    sum = sum + mark[i]
  return sum/len(mark)

def higher(m):
  count = 0
  for i in range(0, len(mark)):
    if mark[i] > m:
      count += 1
  return count
  
print(average())
print(higher(99))