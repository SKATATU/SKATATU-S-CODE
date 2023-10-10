ttt = [[0,0,0],[0,0,0],[0,0,0]]

def DefendMap():
  for i in range(0,3):
    for j in range(0,3):
      ttt[i][j]=0

def ShowMap():
  for i in range(0,3):
    for j in range(0,3):
      if ttt[i][j]==1:
        print("o", end ="")
      elif ttt[i][j]==2:
        print("x", end ="")
      else:
        print("-", end ="")
    print("")  

def Switchturn(currentTurn):
  if currentTurn==1:
    return 2
    print("It's player 2's turn")
  else:
    return 1
    print("It's player 1's turn")


def CheckEnd():
  for i in range(0,3):
    for j in range(1,3):
      if ttt[i][0]==j and ttt[i][1]==j and ttt[i][2]==j:
        return j
      if ttt[0][i]==j and ttt[0][i]==j and ttt[0][i]==j:
        return j
  for i in range (1,3):
    if ttt[0][0] == i and ttt[1,1]== i and ttt[2,2]==i:
      return i 
    if ttt[0][2] == 1 and ttt [1,1] == i and ttt[2,0] == i:
      return i
  cnt = 0
  for i in range (0,3):
    for j in range (0,3):
      if ttt[i][j]!=0:
        cnt+=1
  if cnt == 9:
    return 3
  return 0
      
  

  
def GetPlayerInput():
  inputXY=("What is the XY-axis? :")
  inpX=int(inputXY[0])
  inpY=int(inputXY[1])
  return inpX , inpY
def ShowResult():
  if mode == 3:
    print("It's a draw!")
  if mode == 1:
    print("Player 1 wins!")
  if mode == 2:
    print("Player two wins!")
  if mode == 0: 
    print("PLease continue!")
    
    

DefendMap()
currentTurn=1
mode=0
while mode == 0 :
  row,col = GetPlayerInput()
  ttt[row][col] = currentTurn
  mode = CheckEnd()
  currentTurn = Switchturn(currentTurn)
  ShowMap()


ShowResult()
