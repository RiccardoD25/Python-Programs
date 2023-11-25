def snackBarMenu():
    
    #Declaring constants to store prices
    PIZZA_PRICE=6.0
    PRETZEL_PRICE=2.50
    CHIPS_PRIZE=1.25
    HOTDOG_PRICE=3.75
    current_total=0.0
    #printing welcome message
    print("Welcome to Yum Yum Snack Bar!")
    #while loop to iterate until customer enter 5 as choice
    while True:
        #printing menu..str(variable) will convert variable as string to concatenate to the print
        print()
        print("Please choose from the following menu:")
        print("1) Personal Pizza $"+str(PIZZA_PRICE))
        print("2) Pretzel $"+str(PRETZEL_PRICE))
        print("3) Chips $"+str(CHIPS_PRIZE))
        print("4) Hot Dog $"+str(HOTDOG_PRICE))
        print("5) Exit")
        print()
        #exception handling block to throw error when invalid type entered
        try:
            #asking customer to input the choice and convert it to integer
            choice=int(input("Enter your choice here:"))
            #this will check for valueerror exceptiona and print the message..continue statement will skip current loop and move to next cycle
        except ValueError:
            print("Not an Integer")
            continue
        #if-elif block to check the entered choice and add its corresponding price to the variable current_total and print it
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
            #when customer chooses 5 tax and total bill is calculated and printed
        elif choice==5:
            print("Current Total: $"+str(current_total));
            tax=current_total*7.0/100
            print("Sales Tax: $"+str(tax));
            print("Total Bill: $"+str(current_total+tax))
            print("Have a nice day!")
            break;
            #if invalid number is entered then this error will printed
        elif choice<1 or choice >5:
            print("Invalid choice. Must choose 1 - 5. Try again.")

snackBarMenu()
    
