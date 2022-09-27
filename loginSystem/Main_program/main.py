import time    
UserName = ""
PassWord = ""
LoginTimes = 0
Process = 0
Gerneral_dict = {"" : ""}
SignupTimes = 0
import PP


while LoginTimes <= 5:
  if Process == 0: 
    print("\nEnter CANCEL if you want to stop the process!\n")
    UserName = input("\nEnter Username: ")

  else:
    print("\nEnter CANCEL if you want to stop the process!")
    PassWord = input("\nEnter Password: ") 

    
  if UserName == "CANCEL" or PassWord == "CANCEL":
    print("\nThe process has been cancelled")
    time.sleep(2)
    LoginTimes += 1
    Process = 0
    UserName = ""
    PassWord = ""

  if UserName == "SIGNUP" or PassWord == "SIGNUP":
    a = input("\nPlease enter your Username:")
    Gerneral_dict.update({"username_set" : a })
    b = input("\nPlease enter you Password:")
    Gerneral_dict.update({"password_set" : b })

  elif UserName != "" and Process == 0:
    Process += 1
    print("out come 1")
    
  elif UserName == Gerneral_dict.get("username_set") and PassWord == Gerneral_dict.get("password_set") and Process >= 1:
    time.sleep(1)  
    print ("\nLogin successful!")
    time.sleep(1)
    print ("\nWelcome to the -----")
    time.sleep(2)    
    Process = 0
    print("")
    import selection
    
    
  else:
    print ("\nPassword or Username did not match!")
    print ("\nPlease enter the Password or Username again!\n")
    LoginTimes += 1
    
if LoginTimes >= 5:
        print("\nThe program EXIT automatically because of the times login unsuccessful.\n  \n  #Security reason")

"""valuable used:
    LoginTimes
    UserName
    Password
    Process
    """

"""created by 
1.SKATAU
2.Letitia
3.Matty
"""