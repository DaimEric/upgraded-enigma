import sys
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

print ("")

word_input = input("Enter word (case sensitive)")
guesses = ''
turns = 5

while turns > 0:         

    failed = 0             
    for char in word_input:
        if char in guesses:
            print (char)    

        else:
    
            print ("_")     
       
        failed += 1    

        if failed == 0:        
            print ("You won")
            sys.exit()

    guess = input("guess a character:")
    guesses += guess                    

    if guess not in word_input:
        turns -= 1
        print ("Wrong")
        print ("You have", + turns, 'more guesses')

        if turns == 0:
            print ("You Loose")
            break
