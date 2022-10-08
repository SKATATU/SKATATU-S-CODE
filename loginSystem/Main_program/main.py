from encodings import utf_8
import select
from pathlib import Path
from tkinter.tix import Select
import bcrypt
import time

from PP import Password_dict, Username_dict

UserName = ""
PassWord = ""
LoginTimes = 0
Process = 0
SignupTimes = 0

script_dir = Path("/Users/edward/first_git/loginSystem/Main_program/bin_123.txt").parent
bubble_file = script_dir / 'bubble_sort.txt'


def selection():
  print("\n1.bubble_sort.py", "\nenter END to end the process.")
  print("\n2.login_greating.py", "\nenter END to end the process.")
  print("\n3.number_accending.py", "\nenter END to end the process.")
  print("\nenter CANCEL to cancel the selection process.")

  Select = input("\nPlease enter the NUMBER\
  (without .\
  ) from above that the program you would like to see the code.")

  if Select == "1":
    print("")
    file1 = open("bubble_sort.txt")
    file1.read()
    print("")
    print("Selection():Finished process! Goodbye!")
    exit()

  if Select == "2":
    print("")
    file2 = open(r'login_greeting.txt','r')
    file2.read()
    print("")
    print("Selection():Finished process! Goodbye!")
    exit()
  if Select == "3":
    print("")
    file3 = open(r'bubble_sort.txt','r')
    file3.read()
    print("")
    print("Selection():Finished process! Goodbye!")
    exit()
  if Select == "CANCEL":
    exit(selection)



while LoginTimes <= 5:
  if Process == 0: 
    print("\nEnter CANCEL if you want to stop the process!")
    print("Enter SIGNUP if you want to sign up an account!")
    UserName = input("\nEnter Username: ") 


  if UserName == "SIGNUP" or PassWord == "SIGNUP": #the sign up process
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
      print ("\nWelcome to the selection process")
      time.sleep(2)    
      Process = 0
      print("")
      selection() #run the selection proccess
      print("out come 1")
      
    else:
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