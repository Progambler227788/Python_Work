import random
import os

def roll_dice(num_dice=2):
    return [random.randint(1, 6) for _ in range(num_dice)]

def calculate_score(dice):
    if len(dice) == 2 and abs(dice[0] - dice[1]) == 1:
        return min(dice) * 2 + max(dice)
    return sum(dice)

def read_game_history(filename):
    history = {"matches": 0, "user_wins": 0, "computer_wins": 0, "draws": 0}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Match"):
                    history["matches"] += 1
                elif "Computer" in line:
                    history["computer_wins"] += 1
                elif "Draws" in line:
                    history["draws"] += 1
                else:
                    history["user_wins"] += 1
    return history

def write_game_history(filename, history):
    with open(filename, "a") as file:
        file.write(f"Match {history['matches']}\n")
        file.write(f"User {history['user_wins']}\n")
        file.write(f"Computer {history['computer_wins']}\n")
        file.write(f"Draws {history['draws']}\n")

def display_game_history(history):
    print("\nGame History:")
    print(f"Total Matches: {history['matches']}")
    print(f"User Wins: {history['user_wins']}")
    print(f"Computer Wins: {history['computer_wins']}")
    print(f"Draws: {history['draws']}")

def determine_winner(user_score, computer_score, username):
    if user_score > 12 and computer_score > 12:
        return "Draw"
    elif user_score > 12:
        return "Computer"
    elif computer_score > 12:
        return username
    elif user_score == computer_score:
        return "Draw"
    elif user_score > computer_score:
        return username
    else:
        return "Computer"

def main():
    filename = "game_history.txt"
    user_name = input("Enter your name: ")
    know_rules = input("Do you know the rules of the game? (yes/no): ").strip().lower()
    if know_rules != "yes":
        print("The rules are as follows: ...")  # Display the full rules

    history = read_game_history(filename)
    display_game_history(history)
    
    while True:
        print(f"\nStarting a new game...")
        
        user_dice = roll_dice()
        computer_dice = roll_dice()
        
        user_score = calculate_score(user_dice)
        computer_score = calculate_score(computer_dice)
        
        print(f"\n{user_name} rolled {user_dice} with a score of {user_score}")
        print(f"Computer rolled {computer_dice} with a score of {computer_score}")
        
        if user_score > 12 or computer_score > 12:
            winner = determine_winner(user_score, computer_score,user_name)
        else:
            if user_score == computer_score:
                user_dice.append(roll_dice(1)[0])
                computer_dice.append(roll_dice(1)[0])
                user_score = calculate_score(user_dice)
                computer_score = calculate_score(computer_dice)
                winner = determine_winner(user_score, computer_score)
            else:
                if user_score > computer_score:
                    choice = input("Do you want to stick or throw again? (stick/throw): ").strip().lower()
                    if choice == "throw":
                        user_dice.append(roll_dice(1)[0])
                        user_score = calculate_score(user_dice)
                else:
                    if computer_score in [9, 10, 11]:
                        choice = "stick"
                    else:
                        choice = "throw"
                    if choice == "throw":
                        computer_dice.append(roll_dice(1)[0])
                        computer_score = calculate_score(computer_dice)
                winner = determine_winner(user_score, computer_score)
        
        print(f"\nFinal Scores - {user_name}: {user_score}, Computer: {computer_score}")
        if winner == "Draw":
            print("It's a draw!")
            history["draws"] += 1
        else:
            print(f"{winner} wins!")
            if winner == "User":
                history["user_wins"] += 1
            else:
                history["computer_wins"] += 1
        history["matches"] += 1
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            write_game_history(filename, history)
            break

if __name__ == "__main__":
    main()
