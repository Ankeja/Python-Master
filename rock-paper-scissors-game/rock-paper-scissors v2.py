#Prints rock, paper scissors
print ("Rock...")
print ("Paper...")
print ("Scissors...")


#Asks each player to input there preferred object
player1 = input ("player1, make your move: ")
player2 = input ("player2, make your move: ")

#basic nested if-elif-else check to see if player1 beats player2. Improved so that if it is a draw the rest of the code will not run. Needs an update to make sure gibberish can't be entered.
if player1 == player2:
    print("it's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper":
    if player2 == "scissors":
        print("player2 wins!")
    elif player2 == "rock":
        print("player1 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("player1 wins!")
    elif player2 == "rock":
        print("player2 wins!")
else:
    print("something went wrong")

