import time
#Must Access this to continue.      
UserName = ""
PassWord = ""
LoginTimes = 0
Process = 0

while LoginTimes <= 5:
  if Process == 0: 
    print("Enter CANCEL if you want to stop the process!\n")
    UserName = input("Enter Username: ")
  else:
    print("Enter CANCEL if you want to stop the process!")
    PassWord = input("Enter Password: ")
    print(PassWord)
  if UserName == "CANCEL" or PassWord == "CANCEL":
    print("The process has been cancelled")
    time.sleep(2)
    LoginTimes += 1
    Process -= 1
    UserName = ""
    PassWord = ""
  elif UserName == "Example" and Process == 0:
    Process += 1
  elif PassWord == "Example" and Process >= 1:
    time.sleep(1)  
    print ("Login successful!")
    time.sleep(1)
    print ("Welcome to the -----")
    time.sleep(2)    
    Process = 0
  else:
    print ("Password or Username did not match!")
    LoginTimes += 1
    
if LoginTimes >= 5:
        print("The program exit automatically because of the  times login unsuccessful. \n #Security reason")

"""
valuable used:
    LoginTimes
    UserName
    Password
    Process
    """

"""
created by 
    1.SKATAU
    2.Letitia
    3.Matty
    4.Dominic
"""
