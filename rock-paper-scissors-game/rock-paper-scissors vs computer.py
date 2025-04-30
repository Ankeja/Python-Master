
from random import randint #imports randint for use

#Prints rock, paper scissors
print ("Rock...")
print ("Paper...")
print ("Scissors...")


#Asks the player to input their preferred object
player1 = input ("player1, make your move: ")
#Generates a random integer between 1 and 3, assigns it to the variable choices and designates the relevant item as player2's choice 
randomNumber = randint(1,3)
choices = {1: "rock", 2: "paper", 3: "scissors"}
player2 = choices[randomNumber]
print ("player 2 chose ", player2)

'''Colts solution (i tried to do it myself rater than just follow along with the video)
rand_num = random.randint(0,2)
if rand_num = o:
    player2 = "rock"
elif rand_num= 1:
    player2 = "paper"
else:
    player2 = "scissors"
print(player2)
'''

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

