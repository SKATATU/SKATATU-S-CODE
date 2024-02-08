import random
puzzle = [[1,2,3],[4,5,6],[7,8,0]]
spaceR=2
spaceC=2
move = 0
detecting = True
win = False
def printPuzz():
  for i in range (0,3):
    for j in range (0,3):
       print (puzzle[i][j],end='')
    print(" ")      
def moveStep():
  global spaceR
  global spaceC
  global move
  if move == 1:
    if spaceR != 0:
      puzzle[spaceR][spaceC], puzzle[spaceR - 1][spaceC]  = puzzle[spaceR - 1][spaceC], 0
  if move == 2:
    if spaceC != 0:
      puzzle[spaceR][spaceC], puzzle[spaceR][spaceC - 1] = puzzle[spaceR][spaceC - 1], 0
  if move == 3: 
    if spaceC != 2:
      puzzle[spaceR][spaceC], puzzle[spaceR][spaceC + 1] = puzzle[spaceR][spaceC + 1], 0
  if move == 4:
    if spaceR != 2:
      puzzle[spaceR][spaceC], puzzle[spaceR + 1][spaceC] = puzzle[spaceR + 1][spaceC], 0
  for i in range (0,3):
    for j in range (0,3):
      if puzzle[i][j] == 0:
         spaceR = i
         spaceC = j
def checkWin():
  global win
  if puzzle == [[1,2,3],[4,5,6],[7,8,0]]:
    win = True
def getInput():
  global move
  print("How do you want to move the '0'?")
  key = input("-------------------------->")
  if key == "I" or key == "i":
    move =  1
  if key == "J" or key == "j":
    move =  2
  if key == "l" or key == "L":
    move =  3
  if key == "K" or key == "k":
    move =  4      
def ShufflePuzz():
  global move
  global spaceR
  global spaceC
  for k in range (0,3):
    for j in range (0,3):
      if puzzle[k][j] == 0:
        spaceR = k
        spaceC = j 
  #detecting loop
  print(spaceR, ",", spaceC)
  move = 1
  for i in range (0, 10):
    moveStep()
    move = random.randint(1,4)
    for k in range (0,3):
     for j in range (0,3):
       if puzzle[k][j] == 0:
         spaceR = k
         spaceC = j
def replay():
  rep = input("Do you want to replay the game? (Y/N)")
  if rep == "Y":
    startProcess()
  elif rep == "N":
    print("Thank you for playing!")
def startProcess():
  global win
  win = False
  print(move)
  printPuzz()
  print("-------------------------->")
  ShufflePuzz()
  print("-------------------------->")
  while win == False:
    printPuzz()
    print("-------------------------->")
    print(spaceR, "," ,spaceC)
    getInput()
    print("move",move)
    print("-------------------------->")
    moveStep()
    checkWin()
  print("Congratulation! You won!\n")
  replay()
#main loop (idk if i should call it a loop, since its only one line now):  
startProcess()
