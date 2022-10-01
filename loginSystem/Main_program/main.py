
import time

from PP import Password_dict, Username_dict


UserName = ""
PassWord = ""
LoginTimes = 0
Process = 0

SignupTimes = 0


while LoginTimes <= 5:
  if Process == 0: 
    print("\nEnter CANCEL if you want to stop the process!")
    print("\nEnter SIGNUP if you want to sign up an account!")
    UserName = input("\nEnter Username: ")


  else:
    print("\nEnter CANCEL if you want to stop the process!")
    print("\nEnter SIGNUP if you want to sing up an account!")
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
    Username_dict.update({"username_set" : a })
    b = input("\nPlease enter you Password:")
    Password_dict.update({"password_set" : b })

  elif UserName != "" and Process == 0:
    Process += 1
    
  elif UserName == Username_dict.get("username_set") and \
  PassWord == Password_dict.get("password_set") \
  and Process >= 1:
    time.sleep(1)  
    print ("\nLogin successful!")
    time.sleep(1)
    print ("\nWelcome to the -----")
    time.sleep(2)    
    Process = 0
    print("")
    print("out come 1")
    import selection
    print("out come 2")

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
    Username_dict
    Password_dict
    username_set
    password_set
    file1
    file2
    file3
    """

"""created by 
1.SKATAU
2.Letitia
3.Matty
4.Dominic
"""