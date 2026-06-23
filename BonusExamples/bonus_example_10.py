try:
    width = float(input("Width: "))
    length = float(input("Length: "))

    if width == length:
        exit("That looks like a square")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")