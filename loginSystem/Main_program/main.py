from encodings import utf_8
import bcrypt
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
    print("Enter SIGNUP if you want to sign up an account!")
    UserName = input("\nEnter Username: ") 

  if UserName == "CANCEL" or PassWord == "CANCEL":
    print("\nThe process has been cancelled")
    time.sleep(2)
    LoginTimes += 1
    Process = 0
    UserName = ""
    PassWord = ""

  if UserName == "SIGNUP" or PassWord == "SIGNUP":
    UserName = input("\nPlease enter your Username:")
    Username_dict.update({"username_set" : UserName })

    PassWord = input("\nPlease enter you Password:")
    hashed_PassWord = bcrypt.hashpw(PassWord.encode('utf-8'),bcrypt.gensalt())
    Password_dict.update({"password_set" : hashed_PassWord })
  else:
    print("\nEnter CANCEL if you want to stop the process!")
    print("Enter SIGNUP if you want to sign up an account!")
    PassWord = input("\nEnter Password: ")
  
  if UserName != " " and Process == 0:
    Process += 1
    print("out come 3")
    
  if UserName == Username_dict.\
get("username_set") and \
Process >= 1:
    print("outcome 4")
    bytePwd = PassWord.encode('utf-8')
    if bcrypt.checkpw(bytePwd,Password_dict.get("password_set")):
      time.sleep(1)  
      print ("\nLogin successful!")
      time.sleep(1)
      print ("\nWelcome to the -----")
      time.sleep(2)    
      Process = 0
      print("")
      print("out come 1")
      import selection_
      print("out come 2")
      exit()

  else:
    print ("\nPassword or Username did not match!")
    print ("Please enter the Password or Username again!\n")
    LoginTimes += 1
    
if LoginTimes >= 5:
        print("\nThe program EXIT automatically because of the times login unsuccessful.\n  \n  #Security reason")
        exit()

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