def mealcost_algorithm():

    # 1. Intro
    
    print("\nAll you can eat American Buffet!!!\nCome and enjoy some of our delicious meals. You wont be disapointed!!!")
    print()

    # 2. Enter the customer's name
    
    name = input("Hiya, what is your name?: ")
    print("Hi",name,".")
    print()

    # 3. Enter the cost for the meal and drink

    meal = float(input("How much is your meal?: "))
    drink = float(input("And how much is your drink?: "))
    print()

    # 4. Calculate the cost for food and drink

    total = meal + drink

    # 5. Display total without taxes and tip
    
    print("I am calculating the amount for your whole meal and your drink is $",format(meal,'.2f'),'+ $',
          format(drink,'.2f'), "which equals to: $",format(total,'.2f'))
    print()
    
    #7. Final calculation with taxes and tip
    
    tax_rate = 0.07
    tip_rate = 0.20
    first = total + (total * tax_rate) + (total * tip_rate)

    print("This is your total bill amount: $",first,", which includes 7% tax and 20% tip. \nThank you for choosing, 'All you can eat American Buffet', please come back soon!!!")
        
mealcost_algorithm()

