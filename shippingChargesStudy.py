def shippingCharges():
    package=float(input("Enter the weight of your package: "))

    if package<=2:
        rate=1.50
        print("The price of your package is $",format(rate,'.2f'))

    elif package >=3 and package <=6:
        rate=3.00
        print("The price of your package is $",format(rate,'.2f'))

    elif package>=7 and package<=10:
        rate=4.00
        print("The price of your package is $",format(rate,'.2f'))
        
    else:
        rate=4.75
        print("The price of your package is $",format(rate,'.2f'))

shippingCharges()
