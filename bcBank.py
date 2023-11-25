def bcBank():
    
    #Ask the user to enter the amount to invest (amToInv)
    amToInv=float(input("Please enter the amount you want to invest: "))
    
    #Based on the amToInv calculate and print the investment plus interest (invPlusInt) for the year
    if amToInv>=0 and amToInv<=19999:
        print("The minimum investment amount is $20,000.")
    elif amToInv>=20000 and amToInv<=49999:
        invPlusInt=0.15*amToInv
        print("Your interest total $",invPlusInt)
        invPlusInt=0.15*amToInv+amToInv
        print("Your investment plus interest total $",invPlusInt)
    elif amToInv>=50000 and amToInv<=99999.99:
        invPlusInt=0.20*amToInv
        print("Your interest total $",invPlusInt)
        invPlusInt=0.20*amToInv+amToInv
        print("Your investment plus interest total $",invPlusInt)
    elif amToInv>=100000 and amToInv<=199999.99:
        invPlusInt=0.25*amToInv
        print("Your interest total $",invPlusInt)
        invPlusInt=0.25*amToInv+amToInv
        print("Your investment plus interest total $",invPlusInt)
    else:
        invPlusInt=0.30*amToInv
        print("Your interest total $",invPlusInt)
        invPlusInt=0.30*amToInv+amToInv
        print("Your investment plus interest total $",invPlusInt)
bcBank()
        
    
        
    
