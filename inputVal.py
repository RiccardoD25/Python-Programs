def inputVal():
    highLimit=int(input("Enter the highest number to count to"))
    while highLimit<1:
        print("value less than one are not allowed")
        highLimit=int(input("Enter the highest number to count to"))



    for count in range (1,highLimit+1):
        print(count)
    print("done")
inputVal()
