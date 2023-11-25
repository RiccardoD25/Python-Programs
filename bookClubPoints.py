def bookClubPoints():
    nBooks=int(input("Enter the number of books for this month: "))
    if nBooks >=0 and nBooks <=1:
        points=0
    elif nBooks >=2 and nBooks <=3:
        points=5
    elif nBooks >=4 and nBooks <=5:
        points=15
    elif nBooks >=6 and nBooks <=7:
        points=30
    elif nBooks >=8:
        points=60

    else:
        print("invalid point value")
        points=0
    print("number of points awarded are",points)
bookClubPoints()
