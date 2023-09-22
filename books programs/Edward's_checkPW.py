username = ""
user = ["edward","edward123"]

def hasDigit():
  for i in range(0, len(username)):
    if ord(username[i]) >= 0 and ord(username[i]) <= 57:
      return True
  return False

def noSpace():
  for i in range(0, len(username)):
    if username[i] == ' ':
      return True
  return False

def checkExist():
  for i in range (0,len(user)):
    if username == user[i]:
      return False
  return True

def checkUsername(): #check for valid usernam
  global username
  username = input("Please enter your username:")
  while hasDigit() ==  False or noSpace() == True or checkExist() == False:
    print("not valid, please enter again")
    return False
   
  print("Your username is valid")
  return True

checkUsername()