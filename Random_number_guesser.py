from random import randint
import os
clear = lambda: os.system("cls") # handle the clear screen for optics

class Game:
    def __init__(self):
        # initialize the variables i use for the whole game
        self.game_running: bool = False
        self.number: int = None
        self.user_input: str = None

    def get_random_number(self) -> int:
        """
        creates a random number between 1 to 10 and returns it
        """
        return randint(1, 10)

    def run(self) -> None:
        # Ask if User wants to play
        self.user_input = input("Do you want to play?\n[Y] or [N]\n>").strip().lower()
        if self.user_input == "y":
            self.game_running = True
        else:
            # Quit the game
            print("Goodbye!")
            return

        # Game loop
        while self.game_running:
            self.number = self.get_random_number()
            
            # Guess the number between 1-10
            while True:
                try:
                    self.user_input = input("Guess a number between 1-10\n>").strip()
                    clear()
                    guess = int(self.user_input)
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    continue

                if guess < self.number:
                    print("Wrong! Select a BIGGER number!")
                elif guess > self.number:
                    print("Wrong! Select a SMALLER number!")
                else:
                    break
                
            # Ask if User wants to play again
            self.user_input = input("Correct! You got the right number!\nDo you want to play again?\n[Y] or [N]\n>").strip().lower()
            clear()
            if self.user_input != "y":
                self.game_running = False
                print("Thanks for playing!")

if __name__ == "__main__":
    game = Game()
    game.run()
