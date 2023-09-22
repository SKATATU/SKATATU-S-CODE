username = ""
user=["michael2","alex123","123rocket","aiden3","eoulapa198"]

def hasDigit():
  for i in range(0, len(username)):
    if username[i] >= '0' and ord(username[i]) <= 57:
      return True
  return False

def noSpace():
  for i in range(0, len(username)):
    if username[i] == ' ':
      return False
  return True

def CheckExist():
  for i in range (0, len(user)):
    if username == user[i]:
      return True
  return False

def CheckUsername(): #check for valid username
  if hasDigit() and noSpace() and not CheckExist():
    return True
  else:
    return False
  
  
isValid=False
while not isValid:
  username = input("Input your username: ")
  if not CheckUsername():
    print("Invalid name")
  else:
    isValid=True
print("Valid")