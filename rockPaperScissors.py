import random
def computerMove():
    move=random.randint(0,2)
    return move
def playerMove():
    moveStr=input("Enter your move(rock, paper, scissors)")
    while validateMoveStr(moveStr)==-1:
        moveStr=input("Enter your move(rock, paper, scissors)")
    return validateMoveStr(moveStr)

def validateMoveStr(moveStr):
    if moveStr=="rock":
        return  0
    elif moveStr=="paper":
        return 1
    elif moveStr=="scissors":
        return 2
    else:
        return -1
def printWinner(computerMove,playerMove):
    if computerMove==playerMove:
        print("It is a draw")
    elif computerMove==0 and playerMove==1:
        print("player Wins!")
    elif computerMove==0 and playerMove==2:
        print("Computer Wins!")
    elif computerMove==1 and playerMove==0:
          print("Computer Wins!")
    elif computerMove==1 and playerMove==2:
         print("player Wins!")
    elif computerMove==2 and playerMove==0:
        print("Player Wins!")
    else:
        print("Computer Wins!")
def showMove(move):
    if move==0:
        return "Rock"
    elif move==1:
        return "Paper"
    else:
        return "Scissors"
def playRPS():
    cM=computerMove()
    
    pM=playerMove()
    print("Computer Plays",showMove(cM))
    print("Player Plays",showMove(pM))
    printWinner(cM,pM)
    
playRPS()
    

    
