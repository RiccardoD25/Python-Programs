def firstMenu():
    
    # Playing rock paper scissors
    menuValid=True
    while menuValid: 
        # Show Menu
        print("1) Show rules")
        print("2) Play the game")
        print("3) Exit")
        # User chooses an option
        choice = int(input("Choose from menu(1-3): "))
        while choice<1 or choice>3:
            print("Menu choices are between 1 and 3")
            choice = int(input("Choose from menu(1-3): "))
        # Program acts in response to choice
        if choice==1:
            print("Rock beats siccors, scissors beats paper, paper beats rock")
        elif choice==2:
            print("Playing the game")
        elif choice==3:
            print("Good bye")
            menuValid=False
##        else:
##            print("Invalid choice")
##        

        
firstMenu()
          
