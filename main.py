import random

class RPSTournament:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.score = {"Player": 0, "Computer": 0}

    def play_round(self, player_move):
        computer_move = random.choice(self.moves)
        print(f"Computer chose: {computer_move}")
        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "paper" and computer_move == "rock") or \
             (player_move == "scissors" and computer_move == "paper"):
            print("You win!")
            self.score["Player"] += 1
        else:
            print("You lose!")
            self.score["Computer"] += 1
        print(f"Score -> Player: {self.score['Player']}, Computer: {self.score['Computer']}")

    def start_game(self):
        print("Welcome to RPS Tournament!")
        while True:
            player_move = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
            if player_move == "exit":
                break
            elif player_move not in self.moves:
                print("Invalid move!")
            else:
                self.play_round(player_move)
        print("Game Over! Final Scores:")
        print(f"Player: {self.score['Player']} | Computer: {self.score['Computer']}")

# Example Usage
game = RPSTournament()
game.start_game()
