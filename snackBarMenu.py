def snackBarMenu():
    
    #constant price list
    PIZZA_PRICE=6.0
    PRETZEL_PRICE=2.50
    CHIPS_PRIZE=1.25
    HOTDOG_PRICE=3.75
    current_total=0.0
    
    print("Welcome to Yum Yum Snack Bar!")
    
    while True:
        #printing menu variables to the print
        print()
        print("Please choose from the following menu:")
        print("1) Personal Pizza $"+str(PIZZA_PRICE))
        print("2) Pretzel $"+str(PRETZEL_PRICE))
        print("3) Chips $"+str(CHIPS_PRIZE))
        print("4) Hot Dog $"+str(HOTDOG_PRICE))
        print("5) Exit")
        print()
        #throw error when invalid type entered
        try:
          
            choice=int(input("Enter your choice here:"))
            
        except ValueError:
            print("Not an Integer")
            continue
        
        #entered choice and add its corresponding price to the variable current_total 
        if choice==1:
            current_total+=PIZZA_PRICE
            print("Current Total: $"+str(current_total));
        elif choice==2:
            current_total+=PRETZEL_PRICE
            print("Current Total: $"+str(current_total));
        elif choice==3:
            current_total+=CHIPS_PRIZE
            print("Current Total: $"+str(current_total));
        elif choice==4:
            current_total+=HOTDOG_PRICE
            print("Current Total: $"+str(current_total));
            
            #chooses 5 tax and total bill is calculated and printed
        elif choice==5:
            print("Current Total: $"+str(current_total));
            tax=current_total*7.0/100
            print("Sales Tax: $"+str(tax));
            print("Total Bill: $"+str(current_total+tax))
            print("Have a nice day!")
            break;
            #error will printed for invalid choice
        elif choice<1 or choice >5:
            print("Invalid choice. Must choose 1 - 5. Try again.")

snackBarMenu()
    
