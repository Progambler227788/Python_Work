import random
import os

"""
    Rolls two dice and returns a list of two numbers.

    Returns:
        list: A list of two numbers, each in the range of 1 to 6.
"""
def roll_dice(num_dice=2):
    a = random.randint(1, 6)
    
    
    if num_dice == 1:
        return [a]
    
    b = random.randint(1, 6)
    
   
    if a == b:
        return [a, a]
    else:
        return [a, b]
    


"""
    Returns the minimum value from a list of two elements.

    Parameters:
        dice (list): A list of two elements.

    Returns:
        int: The minimum value from the list.
"""
def returnMinimum(dice):
    if dice[0] < dice[1]:
        return dice[0]
    else:
        return dice[1]
"""
    Returns the maximum value from a list of two elements.

    Parameters:
        dice (list): A list of two elements.

    Returns:
        int: The maximum value from the list.
"""

def returnMaximum(dice):
    if dice[0] > dice[1]:
        return dice[0]
    else:
        return dice[1]
"""
    Calculates the sum of all the elements in the given list of dice.

    Parameters:
        dice (list): A list of integers representing the dice.

    Returns:
        int: The sum of all the elements in the dice list.
"""  

def getSum(dice):
    sum = 0
    for i in dice:
        sum += i
    return sum


"""
    Calculates the score based on the provided dice values.

    Parameters:
        dice (list): A list of integers representing the dice.

    Returns:
        int: The calculated score based on specific conditions.
        If dice is a pair and the difference is 1 or -1, the score is the sum of the dice like minimum muliplied by 2 and added to maximum dice.
        ELse, the score is the sum of the dice number.
"""


def calculate_score(dice):
    
    first = dice[0]
    second = dice[1]
    
    # print (' First Dice: {} Second Dice: {}'.format(dice[0],dice[1]))
    
    # print(f'Length : {len(dice)}')
    
    ranging = (1,-1)  # in sequence like 4-3 is 1 and 3-4 is -1 so like that
    
    res = (first  - second)
    
    if len(dice) == 3:  # in case of one more roll
        # like i've 3,4,5 in list than 3,4 difference is -1 and 4,5 also -1
        # print (' First Dice: {} Second Dice: {} Third Dice: {}'.format(dice[0],dice[1],dice[2]))
        
        if ( abs(dice[0]-dice[1]) in ranging ) and   (abs(dice[1]-dice[2]) in ranging): 
           return -1  # declaring specific player-computer as winner
        return dice[2]
    
    if len(dice) == 2 and  (  res in ranging  ):
        return returnMinimum(dice) * 2 + returnMaximum(dice)
    
    
    
    return  getSum(dice)

def read_game_history(filename):
    # create a dictionary to store matches user wins, computer wins draws
    # Dictionary is better because it will help us to avoid making different variables
    history_being_created = {"user_wins": 0, "computer_wins": 0, "draws": 0, "latest_match": 0}
    if os.path.exists(filename):  
        with open(filename, "r") as file:  # open file in read mode as we need to see old history
            lines = file.readlines()  # store all lines in lines variable
            if len(lines) == 0:
                return history_being_created
            for line in lines:
                # Read matches
                if line.startswith("Match"):
                    num = ""
                    
                    for i in range(6, len(line) ):
                        if line[i].isnumeric():
                          num += line[i]
                    history_being_created["latest_match"] = int(num)
                    
                     # Read computers wins
                elif "Computer" in line:
                    num = ""
                    for i in range(9, len(line) ):
                        if line[i].isnumeric():
                          num += line[i]
                    history_being_created["computer_wins"] += int(num)
                   
                    
                     # Read draws done
                elif "Draws" in line:
                    num = ""
                    draw = len("Draw")
                    for i in range(draw+2, len(line) ):
                        if line[i].isnumeric():
                           num += line[i]
                    history_being_created["draws"] += int(num)
                   
                     # Read user wins
                elif line[0].isalnum():
                   
                    count = 0
                    # get number after user name that will be after space
                    for i in range(len(line)):
                        if line[i] == " ": # for space
                            count += 1
                            break
                        count += 1 # count characters from user name and have space
                    num = ""
                
                    for m in range(count, len(line)):
                        if line[m].isnumeric():
                             num += line[m]
                    
                    history_being_created["user_wins"] += int(num)  # convert string to num
                
                    
    
    return history_being_created


#  function to write game history
"""
    Writes the game history to a file.

    Args:
        filename (str): The name of the file to write the history to.
        history_being_created (dict): A dictionary containing the game history.
            It should have the following keys:
            - 'matches' (int): The total number of matches played.
            - 'user_wins' (int): The number of wins for the user.
            - 'computer_wins' (int): The number of wins for the computer.
            - 'draws' (int): The number of draws.
        username (str): The username of the player.

    Returns:
        None

    This function takes the game history and the username as input and writes it to a file.
    The file is opened in append mode, so the history is added to the existing file if it exists.
    Each line in the file represents a match and contains the following information:
    - Match <match_number>
    - <username> <user_wins>
    - Computer <computer_wins>
    - Draws <draws>
"""
def write_game_history(filename, history_being_created, username):
    with open(filename, "a") as file:
        file.write(f"Match {history_being_created['latest_match']}\n")
        file.write(f"{username} {history_being_created['user_wins']}\n")
        file.write(f"Computer {history_being_created['computer_wins']}\n")
        file.write(f"Draws {history_being_created['draws']}\n")
        
        
        
"""
    Display the game history.

    Args:
        history_being_created (dict): A dictionary containing the game history.
            It should have the following keys:
            - 'matches' (int): The total number of matches played.
            - 'user_wins' (int): The number of wins for the user.
            - 'computer_wins' (int): The number of wins for the computer.
            - 'draws' (int): The number of draws.

    Returns:
        None

    This function prints the game history to the console. It displays the total number of matches,
    the number of wins for the user, the number of wins for the computer, and the number of draws.
    After printing the history, it resets the user_wins, computer_wins, and draws counters to 0.
    """  

def display_game_history(history_being_created):
    print("\nGame History:")
    print(f"Total Matches: {history_being_created['latest_match']}")
    print(f"User Wins: {history_being_created['user_wins']}")
    print(f"Computer Wins: {history_being_created['computer_wins']}")
    print(f"Draws: {history_being_created['draws']}")
    history_being_created['user_wins'] = 0
    history_being_created['computer_wins'] = 0
    history_being_created['draws'] = 0



"""
    Determines the winner of a game based on the scores of the user and the computer.

    Args:
        user_score (int): The score of the user.
        computer_score (int): The score of the computer.
        username (str): The username of the user.

    Returns:
        str: The winner of the game. Possible values are "Draw", "Computer", or the username of the user.

    This function compares the scores of the user and the computer to determine the winner of a game.
    If both scores are greater than 12, the function returns "Draw". If the user's score is greater than 12,
    the function returns "Computer". If the computer's score is greater than 12, the function returns the username
    of the user. If the user's score is greater than the computer's score, the function returns the username of the user.
    If the user's score is equal to the computer's score, the function returns "Draw". Otherwise, the function returns
    "Computer".
"""

def guess_winner(user_score, computer_score, username):
    
    draw = "Draw"
    pc ="Computer"
    
    # in case both scores greater than 12 
    if (user_score > 12 and computer_score > 12):
        return draw
     # user loses in case of his score is greater than 12
    elif user_score > 12:
        return pc
    
    # computer loses in case of his score is greater than 12
    elif computer_score > 12:
        return username
    
    #in case user score is greater than it then user wins
    elif user_score > computer_score:
        return username
    # in case user score is equal to computer score
    elif (user_score == computer_score):
        return draw
    # otherwise computer wins
    else:
        return pc

def main():
    filename = "GAME_HISTORY.txt"
    user_name = input("Hello! Please enter your good name: ")
    user_knows_rules_of_game = input(f"Hey! Warm Welcome {user_name}. Do you know the rules of the game? (yes/no): ").strip().lower()
    if user_knows_rules_of_game != "yes":
        print("Yes, thanks for pressing yes. The rules are as follows below:")  
        print("""
        Rules of Three in a Row:
        1. Each player rolls two dice. If the scores are in direct sequence, the lower number is doubled and added to the larger number. Otherwise, they are simply added together.
        2. If one score is greater than 12, the other player wins. If both scores are greater than 12 or both are 12, it's a draw.
        3. If scores are equal and less than 12, both throw one more die.
        4. If scores are unequal and less than 12, the higher score player can stick or roll one more die.
        5. If all three dice are in a row, the player wins automatically. Otherwise, scores are compared again.
        6. The final winner is determined by the highest score, or a draw is declared if scores are equal.
        """)

    history_being_created = read_game_history(filename)
    
    
    display_game_history(history_being_created)
    
    if history_being_created["latest_match"] == 0:
        history_being_created["latest_match"] = 1
    else:
        history_being_created["latest_match"] = history_being_created["latest_match"] + 1
        
    winner_announced = False
    
    # true is so that in while condition use choses to close
    while True:
        print(f"\nStarting a new game...")
        
        user_dice = roll_dice()  # get user roll
        computer_dice = roll_dice() # get computer dice roll
        
        user_score = calculate_score(user_dice)
        computer_score = calculate_score(computer_dice)
        
        print(f"\n{user_name} rolled {user_dice} with a score of {user_score}")
        print(f"Computer rolled {computer_dice} with a score of {computer_score}")
        
        if user_score > 12 or computer_score > 12:
            winner = guess_winner(user_score, computer_score,user_name)
        else:
            # equal score get 
            if user_score == computer_score:
                user_dice.append(roll_dice(1)[0])
                computer_dice.append(roll_dice(1)[0])
                user_score += user_dice[2]
                computer_score += computer_dice[2]
                winner = guess_winner(user_score, computer_score,user_name)
                
                
                
            else:
                
                # first user then computer
                if user_score > computer_score:
                    # User turn for throw or stick
                    user_choice = input(f"Hey there {user_name}! Do you want to stick or throw again? (stick/throw): ").strip().lower()
                    if user_choice == "throw":
                        # add one more dice
                        user_dice.append(roll_dice(1)[0])
                        user_score_checked = calculate_score(user_dice)
                        # -1 means user got sequenced, three in a row dice
                        if user_score_checked == -1:
                            winner = user_name
                            winner_announced = True
                        else:
                            user_score += user_dice[2]
                            
                                    # Computer turn for throw or stick
                            if computer_score in [9, 10, 11]:
                                computer_choice = "stick"
                            else:
                                computer_choice = "throw"
                                
                            if  computer_choice  == "throw":
                                computer_dice.append(roll_dice(1)[0])
                                computer_score_checked = calculate_score(computer_dice)
                                # -1 means computer got sequenced, three in a row dice
                                if computer_score_checked == -1:
                                    winner = "Computer"
                                    winner_announced = True
                                else:
                                    computer_score += computer_dice[2]
                                    
                                    
                    else: # computer turn in case of sticking
                        if computer_score in [9, 10, 11]:
                                computer_choice = "stick"
                        else:
                                 computer_choice  = "throw"
                                
                        if  computer_choice  == "throw":
                            computer_dice.append(roll_dice(1)[0])
                            computer_score_checked = calculate_score(computer_dice)
                            # -1 means computer got sequenced, three in a row dice
                            if computer_score_checked == -1:
                                winner = "Computer"
                                winner_announced = True
                            else:
                                computer_score += computer_dice[2] 
                      
                      # first computer, then user   
                                 
                elif user_score < computer_score:
                    # if past score of computer is between 9,10,11 then it wil stick with same score
                    # otherwise it will throw
                    if computer_score in [9, 10, 11]:
                        computer_choice  = "stick"
                    else:
                        computer_choice  = "throw"
                        
                    if  computer_choice  == "throw":
                        computer_dice.append(roll_dice(1)[0])
                        computer_score_checked = calculate_score(computer_dice)
                        # -1 means computer got sequenced, three in a row dice
                        if computer_score_checked == -1:
                            winner = "Computer"
                            winner_announced = True
                            
                        else:  # computer throwed so user turn now
                            computer_score += computer_dice[2]
                            
                            user_choice = input(f"Hey there {user_name}! Do you want to stick or throw again? (stick/throw): ").strip().lower()
                            if user_choice == "throw":
                                # add one more dice
                                user_dice.append(roll_dice(1)[0])
                                user_score_checked = calculate_score(user_dice)
                                # -1 means user got sequenced, three in a row dice
                                if user_score_checked == -1:
                                    winner = user_name
                                    winner_announced = True
                                else:
                                    user_score += user_dice[2]
                                    
                
                                    
                    else: # computer sticks so user turn now
                        user_choice = input(f"Hey there {user_name}! Do you want to stick or throw again? (stick/throw): ").strip().lower()
                        if user_choice == "throw":
                             # add one more dice
                             user_dice.append(roll_dice(1)[0])
                             user_score_checked = calculate_score(user_dice)
                             # -1 means user got sequenced, three in a row dice
                             if user_score_checked == -1:
                                 winner = user_name
                                 winner_announced = True
                             else:
                                 user_score += user_dice[2]
            
                  # in case not dice rolled more than than 2 then there is a winner      
        if winner_announced == False:
            winner = guess_winner(user_score, computer_score,user_name)
        # Print final scores scored by users and computer
        print(f"\nFinal Scores - {user_name}: {user_score}, Computer: {computer_score}")
        if winner == "Draw":
            print("It's a draw!")
            history_being_created["draws"] += 1
        else:
            print(f"{winner} wins!")
            if winner ==  user_name:
                history_being_created["user_wins"] += 1
            else:
                history_being_created["computer_wins"] += 1

        
        # strip function is used here to remove empty spaces if any
        wanna_play_again = input("Hey there!! Do you want to play again? (yes/no): ").strip().lower()
        if wanna_play_again != "yes":
            write_game_history(filename, history_being_created, user_name)
            break
        winner_announced = False

if __name__ == "__main__":
    main()
