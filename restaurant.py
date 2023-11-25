def restaurant():
    TAX_RATE=0.075
    TIP_RATE=0.18
    # Intro
    print("Restaurant Bill Generator...")
    print()
    
    # Enter cost of food and drink
    food=float(input("Please enter cost of food:   $"))
    drink=float(input("Please enter cost of drinks: $"))
    print()

    print("Restaurant Bill")
    print("------------------------")
    print()

    # Calculate stateTax
    stateTax=(food+drink)*TAX_RATE
    # Calculate theTip
    theTip=(food+drink)*TIP_RATE
    # Calculate tax & tip
    totalTax=stateTax+theTip
    # Calculate totals
    total=food+drink+totalTax
    # Print amount
    print("cost of Meal: $",format(food+drink,'.2f'))
    print("Tax Amount:   $",format(stateTax,'.2f'))
    print("Tip Amount:   $",format(theTip,'.2f'))
    print("------------------------")
    print("Total:        $",format(total,',.2f'))
restaurant()
