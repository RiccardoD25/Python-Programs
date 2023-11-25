def gradeToLetter():
    grade=float(input("Enter the grade to be translated: "))
    if grade>=90:
        print("You got an A")
    else:# grade less than 90
        if grade>=80:
            print("You got a B")
        else:# Grade less than 80
            if grade>=70:
                print("You got a C")
            else: #Grade less than 70
                if grade>=60:
                    print("You got a D")
                else:# Grade less than 60
                    print("You got an F")
gradeToLetter()
        
            
