from ast import If, Or
import os
import time

from tkinter import END
from xmlrpc.client import boolean

#Must Access this to continue.
def main():
    while True:
        UserName = ""
        PassWord = ""
        A = False
        def Cancel():
            if UserName or PassWord == "CANCEL":
                print("The process has been cancelled")
                A = True
                main()

        print("Enter CANCEL if you want to stop the process!")

        UserName = input ("Enter Username: ")
        
        Cancel()

        PassWord = input ("Enter Password: ")

        Cancel()

        if UserName == "Example" and PassWord == "Example":
            time.sleep(1)
            print ("Login successful!")
            time.sleep(1)
            print ("Welcome to the -----")
            break


        if UserName != "Example" or PassWord != "Example":
            print ("Password did not match!")

main()