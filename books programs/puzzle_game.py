import random
rows, cols = (3,3)
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

#discardable
"""
def detect():
  global detecting
  print("debug detect")
  
#detect if the side is wall
#count loop for detecting loop

  if move == 1:
    if spaceR == 0:
      detecting = False
      print("debug detect01")
  if move == 2:
    if spaceC == 0:
      detecting = False
      print("debug detect01")
  if move == 3:
    if spaceC == 2:
      detecting = False
      print("debug detect01")
  if move == 4:
    if spaceR == 2:
      detecting = False
      print("debug detect01")
"""
      

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

  for i in range (0, 100):
    moveStep()
    move = random.randint(1,4)
    for k in range (0,3):
     for j in range (0,3):
       if puzzle[k][j] == 0:
         spaceR = k
         spaceC = j
  
#main loop:  
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
  
print("Congratulation! You won!")