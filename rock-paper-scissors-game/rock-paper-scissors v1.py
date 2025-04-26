#Prints rock, paper scissors
print ("Rock...")
print ("Paper...")
print ("Scissors...")


#Asks each player to input there preferred object
player1 = input ("player1, make your move: ")
player2 = input ("player2, make your move: ")

#basic if-elif-else check to see if player1 beats player2, will be updated in the future so it is cleaner
if player1 == "rock" and player2 == "scissors":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins!")
elif player1 == player2:
    print("it's a tie!")
else:
    print("something went wrong!")