Peaches = 0.30
Beans = 0.20
ChknPces = 0.50
Socks = 0.75
Bottled_Water = 0.80
Peaches_input = float(input("how many peaches would you like?"))
print ("your peaches will cost £" + str(Peaches_input*Peaches))
Beans_input = float(input("how many Beans would you like?"))
print ("Your Beans will cost £" + str(Beans_input*Beans))
ChknPces_input = float(input("How many Chicken Pieces would you like?"))
print ("Your Chicken Pieces will cost £" + str(ChknPces_input*ChknPces))
Socks_input = float(input("How many Socks would you like?"))
print ("Your Socks will cost this much £" + str(Socks_input*Socks))
Btld_Wtr_input = float(input("How many Bottles of water would you like?" ))
print ("Your Bottles of Water will cost £" + str(Btld_Wtr_input*Bottled_Water))

Multiply = float(Peaches_input*Peaches + Beans_input*Beans + ChknPces_input*ChknPces + Socks_input*Socks + Btld_Wtr_input*Bottled_Water)
print ("This is your overall balance: £" + str(Multiply))
Ttl_Itms = int(Peaches_input + Beans_input + ChknPces + Socks_input + Btld_Wtr_input)
print ("The total amount of Items you bought today is " + str(Ttl_Itms))
