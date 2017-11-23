import random
dice = random.randrange(0, 6) +1
dice_two = random.randrange(0,6)+1
count = 1
while dice!= 6:
    print("Throw dice one:" , dice)
    dice = random.randrange(0,6)+1
    count +=1
while dice_two !=6:
    print("Throw dice two:" , dice_two)
    dice_two = random.randrange(0,6)+1
    count +=1

print("Throw dice one:", dice)
print("Throw dice two:", dice_two)
print("Number of throws:", count)
