def getFinalGrade():
    # Enter score1 score2 score3
    score1=float(input("Enter the value of score for exam 1: "))
    score2=float(input("Enter the value of score for exam 2: "))
    score3=float(input("Enter the value of score for exam 3: "))

    # Calculate finalGrade
    finalGrade=(score1+score2+score3)/3

    # Printing finalGrade
    print("Biology's final grade is",format(finalGrade,'.1f'))
getFinalGrade()
