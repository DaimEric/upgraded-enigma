loop = 1
while loop == 1:
    diamond_width = int(input("Enbter the width: "))
    diamond_height = (diamond_width) * 2 + 1
    starting_width = -1
    acheived_width = 0
    for length in range (diamond_height):
        print ((starting_width * ("* ")).center(diamond_height), end=" ")

        if starting_width == diamond_width:
            acheived_width = 1
        if acheived_width == 1:
            starting_width = starting_width - 1
        else:
            starting_width = starting_width + 1
        print()
