def romanNumerals():
    number=int(input("Enter the number to be translated to roman number (1-4) "))
    if number ==1:
        print("I")
    if number==2:
        print("II")
    if number==3:
        print("III")
    if number==4:
        print("IV")
    if number<1:
        print("We do not the translation for this number")
    if number>4:
        print("We do not have the transaltion for this number")
romanNumerals()
