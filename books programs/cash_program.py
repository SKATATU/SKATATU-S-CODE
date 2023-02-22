global num
global catCheck
def showMenu():
  print("0.Logout")
  print("1.Cash withdrawal")
  print("2.Transfer")
  print("3.Account balance\n")
  
def module1():
  print("How much would you like to withdraw?\n")
def module2():
  print("How much would you like to transfer?\n")
def module3():
  print("This is your account balance: \n")
def module0():
  print("You have been logged out.\n")

catCheck=0  
showMenu()
num = int(input("Please enter an interger between 0 to 3.\n"))

while num != 0 and catCheck <=3:
  if num == 1:
    module1()
  elif num == 2:
    module2()
  elif num == 3:
    module3()
  else:
    print("Input invalid!\n")
    catCheck += 1
  showMenu()
  num = int(input("Please enter an interger between 0 to 3.\n"))
if num != 0 and catCheck >=3:
  print("You've entered 5 times wrongly, process stopped because of security.\n")
  
module0()
