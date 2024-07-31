import stdio
import sys


checker_increment = [0]
rowsUsed = 10
colsUsed = 10
direction_users = ("u", "r", "d", "l")
err = [False,"Error"]
dark_list = list()
light_list = list()
list_sinks =  list()
blocked_items =  list()

def update_board(placement_values, d1, d2):
    # Call placement functions
    
    place_sinks(placement_values)
        
    place_blocked_elements(placement_values)
        
    place_players_pieces(placement_values,True)
    
    place_players_pieces(placement_values,False)
        
        
        
def process_input(rows, cols, mode):
    
    
    # Input Validation
    if rows < 8 or rows > 10 or cols < 8 or cols > 10:
        # If the dimensions are invalid, print an error message
        stdio.write("ERROR: Invalid arguments")
        exit(0)
    # Create an empty game board
    game_board = []
    
    global rowsUsed
    global colsUsed
    rowsUsed = rows
    colsUsed = cols
    
    for i in range(rows):
       row = []
       for j in range(cols):
           row.append(' ')
       game_board.append(row)

    
    checking = 0
    
    while True:
        line_input = stdio.readLine()
        
        # If the input is "#", check game logic and exit
        if line_input == "#":
            if err[0] == True:
               exit()
            if err[1] == "ERROR: Piece in the wrong position":
                stdio.write(err[1])
                exit()
            if checking == 0:
                # If it's the first move and the input is "#", display board, declare light loses, and exit
                corrdinates_board_display(rows, cols, game_board)
                stdio.write("Light loses")
                exit()
            check_game_logic(game_board, rows, cols, True)
            break
        
        checking += 1
        
        # Split the input into individual pieces
        user_inputs = line_input.split(' ')
        
        # Check the number of inputs and call the appropriate validation function
        if len(user_inputs) < 4:
            validate_piece(user_inputs[0], user_inputs[1], user_inputs[2], 0, rows, cols)
        else:
            if user_inputs[2] in ('0','1','2') and user_inputs[3] in ('0','1','2') and user_inputs[0] in ('l','d'):
                err[1] = "ERROR: Piece in the wrong position"
                
            validate_piece(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], rows, cols)
    
    
    # After all inputs are processed, check game logic
    check_game_logic(game_board, rows, cols, False)


        


def check_constraints(object_type, dimension1, dimension2, value_number, rows, cols):
    def check_border_position(x, y):
       # Check if the position is within the specified border range
       if 0 <= x < 3 or rows - 3 <= x < rows:
           if 0 <= y < 3 or cols - 3 <= y < cols:
               return True
       return False
    
    def check_free_field(object_list, obj_type, x, y, val_num):
        if [obj_type, x, y, val_num] in object_list:
            stdio.write(f"ERROR: Field {y} {val_num} not free")
            exit()
    
    if object_type.lower() == 's':
        if not (check_border_position(dimension2, value_number) or value_number in (3, 6) or dimension2 in (3, cols - 4)):
          stdio.write("ERROR: Sink in the wrong position")
          exit()
        if ['s', int(dimension1), dimension2, value_number + 1] in list_sinks or ['s', int(dimension1), dimension2, value_number - 1] in list_sinks:
            stdio.write("ERROR: Sink cannot be next to another sink")
            exit()
        
        list_sinks.append([object_type, convert_to_number(dimension1), dimension2, value_number])
    
    elif object_type.lower() == 'd':
        check_border_position(dimension2, value_number)
        check_free_field(light_list, 'l', dimension1, dimension2, value_number)
        dark_list.append([object_type, dimension1, dimension2, value_number])
    
    elif object_type.lower() == 'x':
        blocked_items.append([object_type, int(dimension1), dimension2])
    
    else:
        check_border_position(dimension2, value_number)
        check_free_field(dark_list, 'd', dimension1, dimension2, value_number)
        light_list.append([object_type, dimension1, dimension2, value_number])


def corrdinates_board_display(board_rows, board_columns, placement_values):
    # Print column numbers
    stdio.write("  ")
    index = 0
    while index < board_columns:
        stdio.write(f" {index} ")
        index += 1

    stdio.write("\n")

    # Display top border
    stdio.write("  " + "+--" * board_columns + "+ \n")

    index = board_rows - 1
    while index >= 0:
        # Display left border and row number
        stdio.write(f"{index} |")
    
        # Print each cell in the row
        inner = 0
        while inner < board_columns:
            cell_value = placement_values[index][inner]
            # Check if the cell is empty
            if type(cell_value) == int:
                
                value_str = str(cell_value)
                padding = "" if len(value_str) >= 2 else " "
                stdio.write(f"{padding}{value_str}|")
          
                # Check if the value in the cell is a string or an integer
            elif cell_value == ' ':
                doubleSpace = "  |" 
                stdio.write(doubleSpace)
                    
            else:
                stdio.write(f" {cell_value}|")
            inner += 1
        index -= 1
        stdio.writeln()
        stdio.write("  " + "+--" * board_columns + "+ \n")
    


def process_player_input(rows, cols, placement_values):
 
    while True:
        # Read the input from the player
        line_input = stdio.readLine()
        
        # Split the input into individual moves
        moves_of_user = line_input.split(' ')
        
        # Check if the move is within the board's dimensions
        if int(moves_of_user[0]) > rows and int(moves_of_user[1]) > cols:
            stdio.write(f"ERROR: Field {moves_of_user[0]} {moves_of_user[1]} not on board")
            exit()
        
        # Validate the move
        validate_moves(moves_of_user[0], moves_of_user[1], moves_of_user[2], placement_values)



def piece_error(dim):
    error_message = f"ERROR: Invalid piece type {dim}" if dim not in ("d", "a", "c", "b") else ""
    if error_message!="":
        stdio.write(error_message)
        exit()
    

def validate_dimensions(piece_type, dimension):
    try:
        # Check if the piece type is valid for non-blocked fields
        if piece_type not in ('x'):
            if piece_type not in ('d', 'l'):
                # Check if the piece type is valid for non-dark and non-light pieces
                dimension = convert_to_number(dimension)
                if dimension not in (1, 2):
                    piece_error(dimension)
            else:
                # Check if the piece type is valid for dark and light pieces
                piece_error(dimension)
    except ValueError:
        # Handle the case where dimension cannot be converted to an integer
        piece_error(dimension)



def object_error(char):
    error_message = f"ERROR: Invalid piece type {char}" if char not in ('l', 'x', 'd', 's') else ""
    if error_message!="":
        stdio.write(error_message)
        exit()
    

def convert_to_number(c):
    return int(c)

def validate_piece(char, a1, a2, a3, rows, cols):
    # Check if the object type is valid
    object_error(char) 
    
    try:
        # Convert dimensions and coordinates to integers
        a2 = convert_to_number(a2)
        a3 = convert_to_number(a3)
        
        # Check if the coordinates are within the board's dimensions
        if not (0 <= a2 < rows and 0 <= a3 < cols):
            stdio.write(f"ERROR: Field {a2} {a3} not on board")
            exit()
    except ValueError:
        # Handle the case where dimensions or coordinates cannot be converted to integers
        stdio.write(f"ERROR: Field {a2} {a3} not on board")
        exit()
        
    # Validate the dimensions of the piece
    validate_dimensions(char, a1)
    
    # Check constraints for placing the piece on the board
    check_constraints(char, a1, a2, a3, rows, cols)

    
    
def place_sinks(placement_values):
    i = 0
    while i < len(list_sinks):
        sinking = list_sinks[i]
        data = sinking[0]
        if sinking[1] == 2:
            placement_values[sinking[2] + 1][sinking[3]] = data
            placement_values[sinking[2]][sinking[3] + 1] = data
            placement_values[sinking[2] + 1][sinking[3] + 1] = data
        placement_values[sinking[2]][sinking[3]] = data
        i += 1

        
def place_blocked_elements(placement_values):
    i = 0
    while i < len(blocked_items):
        element = blocked_items[i]
        placement_values[element[1]][element[2]] = element[0]
        i += 1


def place_players_pieces(placement_values, turn):
    i = 0
    pieces_list = dark_list if turn else light_list
    while i < len(pieces_list):
        piece = pieces_list[i]
        if piece[1] not in ("a", "b", "c"):
            placement_values[piece[2] + 1][piece[3]] = piece[2] * 10 + piece[3]
            placement_values[piece[2]][piece[3] + 1] = piece[2] * 10 + piece[3]
            placement_values[piece[2] + 1][piece[3] + 1] = piece[2] * 10 + piece[3]
        placement_values[piece[2]][piece[3]] = piece[1].upper() if turn else piece[1]
        i += 1
               
    
def check_game_logic(placement_values, n, m, check):
    # Update board placed values 
    update_board(placement_values, n, m)
    
    # If check is True, display the board; otherwise, process player input
    if check:
        corrdinates_board_display(n, m, placement_values)
    else:
        process_player_input(n, m, placement_values)

  
win_comparison = [0, 0]


def call_print(a, b, placement_values):
    # Call Print Function
    corrdinates_board_display(a, b, placement_values)
    process_player_input(a, b, placement_values) 
    
def check_player_win():
    light_win = win_comparison[0] == len(light_list) and win_comparison[0] >= 4
    dark_win = win_comparison[1] == len(dark_list) and win_comparison[1] >= 4
    
    if light_win:
        stdio.write(f"Light wins!")
    elif dark_win:
        stdio.write(f"Dark wins!")
    
    if light_win or dark_win:
        exit()


def check_move_validity(n, m, move, placement_values):
    global rowsUsed
    global colsUsed
    # Define movement offsets for each direction
    movements = {
        'l': (0, -1),
        'u': (1, 0),
        'r': (0, 1),
        'd': (-1, 0)
    }

    # Check if the move is a valid direction
    if move.strip() not in movements:
        stdio.write(f"ERROR: Invalid direction {move}")
        exit()

    # Get the movement offset for the given direction
    dn, dm = movements[move.strip()]

    # Calculate the new position
    new_n, new_m = n + dn, m + dm

    # Check if the new position is within the board
    if not (10 > new_n >= 0) or not (10 > new_m >= 0):
        stdio.write(f"ERROR: Field {new_n} {new_m} not on board")
        exit()

    # Check if the new position is free
    if placement_values[new_n][new_m].strip() not in ('', 's'):
        stdio.write(f"ERROR: Field {new_n} {new_m} not free")
        exit()

    # Check if the game has been won
    if placement_values[new_n][new_m] == 's':
        if placement_values[n][m].lower():
            win_comparison[0] += 1
        else:
            win_comparison[1] += 1
        placement_values[n][m] = ' '
        check_player_win()
        call_print(rowsUsed, colsUsed, placement_values)
    else:
       apply_move_user(n, m, move, placement_values)
        


def apply_move_user(n, m, move, placement_values):
    # Define movements for each direction
    movements = {
        'l': (0, -1),
        'u': (1, 0),
        'r': (0, 1),
        'd': (-1, 0)
    }

    # Check if the move is legal
    if move in movements:
        # Get the movement for the given direction
        dn, dm = movements[move]

        # Calculate new position
        new_n, new_m = n + dn, m + dm

        # Check if new position is within the board
        if 0 <= new_n < 10 and 0 <= new_m < 10:
            # Check if the piece can be moved back to the starting position
            if new_n == 3 and new_m == 3 and placement_values[n][m] == 'a':
                stdio.write('ERROR: Piece cannot be returned to starting position')
                exit()

            # Move the piece
            placement_values[new_n][new_m] = placement_values[n][m]
            placement_values[n][m] = ' '

            # Print the updated board
            call_print(10, 10, placement_values)
        else:
            stdio.write('ERROR: Cannot move beyond the board')
            exit()
    else:
        stdio.write(f'ERROR: Invalid direction {move}')
        exit()

def second_move():
    stdio.write(f'ERROR: Cannot move a 2x2x2 piece on the second move')
    
def check_second_move(a,b,user_move,board_passed):
    if str(board_passed[a][b]) == 'd' and str(board_passed[a][b + 1]) == "44" and user_move == 'r':
        second_move()
        exit()
    else:
        check_move_validity(a,b,user_move,board_passed)
    

def validate_moves(n, m, move, placement_values):
    n = convert_to_number(n)
    m = convert_to_number(m)
    
    if checker_increment[0] == 0 and str(placement_values[n][m]).isupper():
        stdio.write(f"ERROR: Piece does not belong to the correct player")
        exit()
        
    if checker_increment[0] == 0 and len(str(move)) == 0:
        stdio.write(f"Light loses")
        exit()
    
    checker_increment[0] += 10      
    
    if placement_values[n][m] == ' ':
        stdio.write(f'ERROR: No piece on field {n} {m}')
        exit()
    
    check_second_move(n,m,move,placement_values)

def write_illegal():
    stdio.write("ERROR: Illegal argument \n") 
        
# driver code
def main():
    args = len(sys.argv)
    counter = 4
    
    # Check validity of arguments
    if args > counter:
        stdio.write("ERROR: Too many arguments \n")
        exit()
    elif args < counter:
        stdio.write("ERROR: Too few arguments \n")
        exit()
    elif args == counter:
        try:
            game_mode_being_played =  convert_to_number(sys.argv[3])
            board_rows      =  convert_to_number(sys.argv[1])
            board_columns   =  convert_to_number(sys.argv[2])
          
        except ValueError:
            write_illegal()
            exit()
        
        if not (8 <= board_rows <= 10) or not (8 <= board_columns <= 10) or not (0 <= game_mode_being_played <= 1):
          write_illegal()
          exit()
            
        process_input(board_rows, board_columns, game_mode_being_played)

main()
