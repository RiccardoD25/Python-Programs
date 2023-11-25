def geometry():
    # Enter input (width and height)
    WIDTH=float(input("Enter width"))
    height=float(input("Enter height"))

    # Calculate atrea
    area=WIDTH*height

    # Print area
    print("Rectangle of",format(WIDTH,'.2f'),"x",format(height,'.2f'),
          "has an area of",format(area,'.2f'))
geometry()
