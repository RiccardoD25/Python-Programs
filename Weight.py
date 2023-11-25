def weight():

    print("500 Less a day make the Weight Go Away ...")
    print('')
    #weight guidlines
    guidelines=True
    while guidelines:
        #Show guidelines
        print("1) 10 ways to cut 500 calories guidelines")
        print("2) Generate next semester expected weight table.")
        print("3) Quit")
        print("")
        #User chooses guidelines
        choice=int(input("Choose one of the following options: "))
        while choice<1 or choice>3:
            print("List choices are from 1 to 3")
            choice=int(input("Choose one of the following options: "))
        #Program will respond to choice selected from 10 statements 
        if choice==1:
            print('* swap your snack. ')
            print('* cut one high-calorie treat.')
            print('* Do not frink your calories.')
            print('* skip seconds. ')
            print('* Make low calorie substitutions.')
            print('* Ask for doggie bag.')
            print('* Just say "no" to fried food.')
            print('* Build a thinner pizza.')
            print('* use a smaller plate.')
            print('* Avoid alcohol.')
            print("")
        #Input user starting weight 
        elif choice==2:
            weight=float(input("Please enter starting weight in pounds: "))
            #If input weight is less than 100 lbs again then it loops until weight is 100 lbs or more
            while weight<100:
                 print("Error, please choose weight higher than 100 lbs")
                 weight=float(input("Please enter starting weight in pounds: "))
            #Table chart print                 
            print('----------------------------------------')
            print('Month Weight ')
            print('----------------------------------------')
            #Table for weight calculations
            for i in range(1,6+1):
                weight=weight-4   
                print(i,' ',weight,' lbs')
        #End the program
        elif choice==3:
            print("Good Bye...")
            guidelines=False

weight()
            
