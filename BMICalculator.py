def BMICalculator():
    #Ask for weight in pounds
    weight=float(input("Enter your weight in pounds: "))
    #Ask for height in inches
    height=float(input("Enter your height in inches: "))
    #Calculate BMI
    BMI=weight*703/height**2
    #Take a decision about overweight, optimal or underweight
    if BMI>25:
        print("Person is overweight")
    elif BMI>=18.5:
        print("person is optimal weight")
    else:
        print("person is underweight")
BMICalculator()
