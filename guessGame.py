##def getGuess(first,last):
##    guess=int(input("Enter your guess ("+str(first)+"-"+str(last)+"): "))
##    while guess<first or guess>last:
##        print("Error...Incorrect number. Try again")
##        guess=int(input("Enter your guess ("+str(first)+"-"+str(last)+"): "))
##    return guess
##print(getGuess(1,100))
import random
def getGuess(first,last):
    guess=int(input("Enter your guess ("+str(first)+"-"+str(last)+"): "))
    while guess<first or guess>last:
        print("Error...Incorrect number. Try again")
        guess=int(input("Enter your guess ("+str(first)+"-"+str(last)+"): "))
    return guess

def guessWin(number,guess):#number is the computer generated guess is for the user
    if number>guess:
        print("Too Low...")
        return False
    elif number<guess:
        print("Too High...")
        return False
    else:
        print("Congratulations... You have guessed the mystery nunber")
        return True
    
def playGame():
    number=random.randint(1,100)
    numOfTries=0
    hasWon=False
    while numOfTries<=7 and hasWon==False:
        guess=getGuess(1,100)
        hasWon=guessWin(number,guess)
        numOfTries=numOfTries+1
    if hasWon==False:
        print("You ran out of tries, sorry you lost")
def main():
    playAgain=True
    while playAgain:
        playGame()
        answer=input("Would you like to try again(y/n) ")
        while answer!="y" and answer!="n":
            print("Valod answers are y or n")
            answer=input("Would you like to try again(y/n) ")
        if answer=="y":
            playAgain=True
        else:
            playAgain=False
        
main()
