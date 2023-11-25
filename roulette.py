def roulette():
     
     #Ask player to enter a number (0-36)
    
    number= int(input("Please enter a pocket number that is (0-36): "))

    if number >= 0 and number <= 36:
        if number == 0:
            color = "Green"

        elif number >= 1 and number <= 10:
            if number % 2 == 0:
                color = "Black"
            else:
                color = "Red"

        elif number >= 11 and number <= 18:
            if number % 2 == 0:
                color = "Red"
            else:
                color= "Black"

        elif number >= 19 and number <= 28:
            if number % 2 == 0:
                color = "Black"
            else:
                color = "Red"

        elif number >= 29 and number <= 36:
            if number % 2 ==0:
                color = "Red"
            else:
                color = "Black"

        print("Pocket color = ", color)
        
    else:
        print("Invalid.. Please enter a valid number that is (0-36)")
                
roulette()
    
