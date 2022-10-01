from main import UserName

print("\n1.bubble_sort.py")
print("\n2.login_greating.py")
print("\n3.number_accending.py")

Select = input("\nPlease enter the NUMBER\
(without .\
) from above that the program you would like to see the code.")

if Select == 1:
    print("")
    file1 = open("buin_123.tst", "r")
    print(file1)
    print("")
    print("Finished process! Goddbye",UserName, "!")
    exit()

if Select == 2:
    print("")
    file2 = open("login_greeting.txt", "r")
    print(file2)
    print("")
    print("Finished process! Goddbye",UserName, "!")
    exit()
if Select == 3:
    print("")
    file3 = open("bubble_sort.txt", "r")
    print(file3)
    print("")
    print("Finished process! Goddbye",UserName, "!")
    exit()

