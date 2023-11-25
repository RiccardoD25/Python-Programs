##Mass and Weight
##
##scientists measure an onjects mass in kilograms and its weight in Newtons.
##If you know the amount of mass that an object has, you can calculate its weight, in newtons,
##with following formula:
##weight = mass X 9.8
##
##write a program thats asks the user to enter an objects mass and then calculate its weight.
##object weighs more than 1,000 Newtons, display a message indicating it is too heavy.
##if object weighs less than 10 Newtons, display e message indicating it is too light.


##def massAndWeight():
##
##    # obtain the mass from user
##    mass=float(input("Enter the Mass in kg. "))
##    # Calculate the weight
##    weight=mass*9.8
##    # Decide based on weight if object is too heavy or too light
##    if weight>1000:
##        print("Object is too heavy.")
##    if weight<10:
##        print("Object is too light.")
##    else:
##        print("object is not too heavy or too light.")
##        
##massAndWeight()


    
##Bank Charges
##A bank chrages a base fee of $10 per month, plus following check fees for commercial checking account:
##
##    $0.10 ea for less than 20 checks
##    $0.08 ea for 20-39 checks
##    $0.06 ea for 40-59 checks
##    $0.04 ea for 60 or more checks
##
##write a program that asks number of checks written fo the month. The program should
##then calculate & display the banks service fees fo the month.

##def bankCharges():
##
##    # Ask user for the number of checks (numOfChecks) written that month
##    numOfChecks=int(input("Enter the number of checks written this month: "))
##    # Based on the numOfChecks calculate and print service fee (serviceFee) for that month
##    if numOfChecks>=0 and numOfChecks<=19:
##        serviceFee=10.0+numOfChecks*0.10
##        print("The monthly service fee is $",serviceFee)
##    if numOfChecks>=20 and numOfChecks<=39:
##        serviceFee=10.0+numOfChecks*0.08
##        print("The monthly service fee is $",serviceFee)
##    if numOfChecks>=40 and numOfChecks<=59:
##        serviceFee=10.0+numOfChecks*0.06
##        print("The monthly service fee is $",serviceFee)
##    if numOfChecks>=60:
##        serviceFee=10.0+numOfChecks*0.04
##        print("The monthly service fee is $",serviceFee)
##        
##bankCharges()


def bankCharges():

    # Ask user for the number of checks (numOfChecks) written that month
    numOfChecks=int(input("Enter the number of checks written this month: "))
    # Based on the numOfChecks calculate and print service fee (serviceFee) for that month
    if numOfChecks>=0 and numOfChecks<=19:
        serviceFee=10.0+numOfChecks*0.10
        print("The monthly service fee is $",serviceFee)
    elif numOfChecks>=20 and numOfChecks<=39:
        serviceFee=10.0+numOfChecks*0.08
        print("The monthly service fee is $",serviceFee)
    elif numOfChecks>=40 and numOfChecks<=59:
        serviceFee=10.0+numOfChecks*0.06
        print("The monthly service fee is $",serviceFee)
    else:
        serviceFee=10.0+numOfChecks*0.04
        print("The monthly service fee is $",serviceFee)
        
bankCharges()

    
##def bankCharges():
##
##    # Ask user for the number of checks (numOfChecks) written that month
##    numOfChecks=int(input("Enter the number of checks written this month: "))
##    # Based on the numOfChecks calculate and print service fee (serviceFee) for that month
##    if numOfChecks>=0 and numOfChecks<=19:
##        feePerCheck=0.1
##        serviceFee=10.0+numOfChecks*feePerCheck
##        
##    elif numOfChecks>=20 and numOfChecks<=39:
##        feePerCheck=0.08
##        serviceFee=10.0+numOfChecks*feePerCheck
##       
##    elif numOfChecks>=40 and numOfChecks<=59:
##        feePerCheck=0.06
##        serviceFee=10.0+numOfChecks*feePerCheck
##        
##    else:
##        feePerCheck=0.04
##        serviceFee=10.0+numOfChecks*feePerCheck
##        
##    print("The monthly service fee is $",serviceFee)
##        
##bankCharges()
##
##
##def bankCharges():
##
##    # Ask user for the number of checks (numOfChecks) written that month
##    numOfChecks=int(input("Enter the number of checks written this month: "))
##    # Based on the numOfChecks calculate and print service fee (serviceFee) for that month
##    if numOfChecks>=0:
##        if numOfChecks>=0 and numOfChecks<=19:
##            feePerCheck=0.1
##            serviceFee=10.0+numOfChecks*feePerCheck
##        
##        elif numOfChecks>=20 and numOfChecks<=39:
##            feePerCheck=0.08
##            serviceFee=10.0+numOfChecks*feePerCheck
##       
##        elif numOfChecks>=40 and numOfChecks<=59:
##            feePerCheck=0.06
##            serviceFee=10.0+numOfChecks*feePerCheck
##        
##        else:
##            feePerCheck=0.04
##            serviceFee=10.0+numOfChecks*feePerCheck
##        
##        print("The monthly service fee is $",serviceFee)
##    else:
##        print("Number of checks cannot be negative")
##        
##bankCharges()


##A mobile service has 3 different subscription packages for its customers:
##    
##package A: 39.99 per month 450 minutes provide. Additional data costs $0.045 /minute.
##package B: 59.99 per month 900 minutes provide. Additional data costs $0.045 /minute.
##package C: 69.99 per month unlimited minutes provided.
##
##write a program that calculates customers monthly bill. Should ask which package the customer has
##purchased and how many mintues were used. It should display total amount due.

def mobileService():

    # packageName, minutes, cost

    # Ask user for package
    packageName=input("Enter customer package: ")
    # Ask user for minutes consumed
    minutes=float(input("Enter minutes consumed: "))
    # Calculate the cost based on... packages

    # Make a decision based on the package
    if packageName=="A":
        if minutes<=450:
            cost=39.99
        else:
            cost=39.99+(minutes-450)*0.45
        print("this month you have to pay $",cost)

    elif packageName=="B":
        if minutes<=900:
            cost=59.99
        else:
            cost=59.99+(minutes-900)*0.40
        print("this month you have to pay $",cost)

    elif packageName=="C":
        cost=69.99
        print("this month you have to pay $",cost)

    else:
        print("Not a valid package")
        
mobileService()
    

