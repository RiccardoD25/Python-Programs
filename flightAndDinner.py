def flightAndDinner():

# Ask passanger for their name

    name=input("Can i get your name please? ")
    print("Hello",name)

# Ask passanger which flght_class they are flying

    flight_class = input("Which class are you flying with us today? ").lower()

    if flight_class == "first":
        flight_class = input("What would like to eat for dinner (Salmon or Steak)? ")
    if flight_class == "salmon":
         print("That will be $20.00 USD, please swipe your card. Thank you. ")
    if flight_class == "steak":
         print("That will be $15.00 USD, please swipe your card. Thank you.")
    if flight_class == "business":
         flight_class = input("What would like to eat for dinner (Chicken or Beef)? ")
    if flight_class== "chicken":
        print("That will be $10.00 USD, please swipe your card. Thank you.")
    if flight_class == "beef":
        print("That will be $8.00 USD, please swipe your card. Thank you.")

# Ask passanger if they want to fly on a different_class

    different_class = input("Would you like to choose a different flight class?(yes/no) ")
    if different_class == "yes":
        flightAndDinner() 
    elif different_class == "no":
        print("Thanks for flying Jetlag Airlines, come back soon!")
    
flightAndDinner()

