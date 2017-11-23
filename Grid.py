width = int(input("Please enter the width: "))
height = int(input("Please enter the Height: "))
for width in range(1, width):
    print(width)
    for height in range (1,height):
        print("{}{}{}".format(width,height))
