def softwareSales():

    package=float(input("Enter the quantity of packages you want to purchase :"))

    if package>=0 and package<=9:
        package=99-0.00
        print("Your package is $",package," and does not include a discount")
    elif package>=10 and package<=19:
        package=99-0.10
        print(" Your package costs $",package," this includes a 10% discount")
    elif package>=20 and package <=49:
        package=99-0.20
        print(" Your package costs $",package," this includes a 20% discount")
    elif package>=50 and package <=99:
        package=99-0.30
        print(" Your package costs $",package," this includes a 30% discount")
    else:
        package=99-0.40
        print(" Your package costs $",package," this includes a 40% discount")
        
softwareSales()

        
