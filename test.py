import stdio
import sys
import stdarray


# Global Data Variables
dark_pieces = []
light_pieces = []
sink_objects = []
blocked_cells = []
player_directions = ("u", "r", "d", "l")


def update_board(placement_values):
    """Update the game board with the latest changes."""
    place_updated_sinks(placement_values)
    place_updated_blocked_elements(placement_values)
    place_updated_dark_pieces(placement_values)
    place_updated_light_pieces(placement_values)


def check_piece_type(row_count, column_count):
    """
    Validates and processes the type of pieces entered by the user on the gaming board.

    Args:
        row_count (int): The number of rows in the gaming board.
        column_count (int): The number of columns in the gaming board.

    Returns:
        None
    """
    # Create an empty gaming board
    board_play = stdarray.create2D(row_count, column_count, ' ')

    # Validate input dimensions
    if not (8 <= row_count <= 10 and 8 <= column_count <= 10):
        stdio.write("ERROR: Invalid dimensions\n")
        return

    # Process user input until '#' is encountered
    while True:
        user_in = stdio.readLine().strip()

        # Check if the input is "#", indicating end of input or game logic check
        if user_in == "#":
            if board_play == [[' '] * column_count for _ in range(row_count)]:
                # If no moves have been made and input is "#", display board and exit
                display_playboard(row_count, column_count, board_play)
                stdio.write("Light loses\n")
                return
            review_updated_game_logic(board_play, row_count, column_count, True)
            break

        # Split the input into individual pieces
        user_input_list = user_in.split()

        # Check the number of inputs and validate
        if len(user_input_list) < 4:
            process_and_validate_constraints(user_input_list[0], user_input_list[1], user_input_list[2], user_input_list[3], row_count, column_count)
        else:
            process_and_validate_constraints(user_input_list[0], user_input_list[1], user_input_list[2], user_input_list[3], row_count,
                             column_count)

    # Check game logic after all inputs are processed
    review_updated_game_logic(board_play, row_count, column_count, False)


errors = [False]


def process_and_validate_constraints(piece_kind, dimension1, dimension2, value_number, num_rows, num_columns):
    """
    Processes and validates the constraints for placing different types of pieces on the game board.

    Args:
        piece_kind (str): The type of piece being placed ('s' for sink, 'd' for dark piece, 'x' for block, 'l' for light piece).
        dimension1 (int): The first dimension of the piece (usually the row index or similar).
        dimension2 (int): The second dimension of the piece (usually the column index or similar).
        value_number (int): The value associated with the piece.
        num_rows (int): The total number of rows in the game board.
        num_columns (int): The total number of columns in the game board.

    Returns:
        errors (list): A list containing error messages, if any.
    """
    errors = []

    if piece_kind.lower() == 's':
        if dimension2 == 0 or dimension2 == num_rows - 1 or dimension2 == 1 or dimension2 == num_rows - 2:
            if value_number == 0 or value_number == num_columns - 1 or value_number == 1 or value_number == num_columns - 2:
                pass
            else:
                stdio.write("ERROR: Sink in the wrong position")
                errors.append("ERROR: Sink in the wrong position")
                exit()
        else:
            stdio.write("ERROR: Sink in the wrong position")
            errors.append("ERROR: Sink in the wrong position")
            exit()

        if any((s[1], s[2]) == (int(dimension1), dimension2 + 1) or (s[1], s[2]) == (int(dimension1), dimension2 - 1) for s in sink_objects):
            stdio.write("ERROR: Sink cannot be next to another sink\n")
            errors.append("ERROR: Sink cannot be next to another sink")

        sink_objects.append([piece_kind, int(dimension1), dimension2, value_number])

    elif piece_kind.lower() == 'd':
        if any((l[1], l[2]) == (int(dimension1), dimension2) for l in light_pieces):
            stdio.write(f"ERROR: Field {dimension2} {value_number} not free\n")
            errors.append(f"ERROR: Field {dimension2} {value_number} not free")

        if dimension2 == 0 or dimension2 == num_rows - 1 or dimension2 == 1 or dimension2 == num_rows - 2:
            stdio.write("ERROR: Piece in the wrong position\n")
            errors.append("ERROR: Piece in the wrong position")
            exit()

        if value_number == 0 or value_number == num_columns - 1 or value_number == 1 or value_number == num_columns - 2:
            stdio.write("ERROR: Piece in the wrong position\n")
            errors.append("ERROR: Piece in the wrong position")
            exit()

        dark_pieces.append([piece_kind, dimension1, dimension2, value_number])

    elif piece_kind.lower() == 'x':
        dimension1 = int(dimension1)
        blocked_cells.append([piece_kind, dimension1, dimension2])

    else:
        if any((d[1], d[2]) == (int(dimension1), dimension2) for d in dark_pieces):
            stdio.write(f"ERROR: Field {dimension2} {value_number} not free\n")
            errors.append(f"ERROR: Field {dimension2} {value_number} not free")

        if dimension2 == 0 or dimension2 == num_rows - 1 or dimension2 == 1 or dimension2 == num_rows - 2:
            stdio.write("ERROR: Piece in an invalid position\n")
            errors.append("ERROR: Piece in an invalid position")
            exit()

        if value_number == 0 or value_number == num_columns - 1 or value_number == 1 or value_number == num_columns - 2:
            stdio.write("ERROR: Piece in the wrong position\n")
            errors.append("ERROR: Piece in the wrong position")
            exit()

        light_pieces.append([piece_kind, dimension1, dimension2, value_number])

    return errors


def display_playboard(num_rows, num_cols, cell_values):
    """
    Displays the game board with the given number of rows and columns along with the cell values.

    Args:
        num_rows (int): The number of rows in the game board.
        num_cols (int): The number of columns in the game board.
        cell_values (list): A 2D list representing the values of each cell in the game board.

    Returns:
        None
    """
    # Print column numbers
    stdio.write("  ")
    col_index = 0
    while col_index < num_cols:
        stdio.write(f" {col_index} ")
        col_index += 1
    stdio.write("\n")

    # Display top border
    stdio.write("  " + "+--" * num_cols + "+ \n")

    # Print each row
    row_index = num_rows - 1
    while row_index >= 0:
        # Display left border and row number
        stdio.write(f"{row_index} |")

        # Print each cell in the row
        col_index = 0
        while col_index < num_cols:
            cell_value = cell_values[row_index][col_index]

            # Check if the cell is empty
            if cell_value == ' ':
                stdio.write("  |")
            else:
                # Check if the value in the cell is a string or an integer
                if isinstance(cell_value, str):
                    # If it's a string, print it with proper formatting
                    stdio.write(f" {cell_value} |")
                elif isinstance(cell_value, int):
                    # If it's an integer, check its length for proper formatting
                    if len(str(cell_value)) < 2:
                        stdio.write(f" {cell_value} |")
                    else:
                        stdio.write(f"{cell_value}|")

            col_index += 1

        # Display the right border of the row
        stdio.write("\n")
        stdio.write("  " + "+--" * num_cols + "+ \n")
        row_index -= 1


def process_user_input_and_validate(height, width, state):
    """
    Processes user input and validates the moves based on the specified game board dimensions and state.

    Args:
        height (int): The height of the game board.
        width (int): The width of the game board.
        state (list): The state of the game board.

    Returns:
        None
    """
    # Iterate over each line of input
    for input_line in stdio.readAll().splitlines():
        # Split the input into individual moves
        user_moves = input_line.split(' ')

        # Check if the number of moves is correct
        if len(user_moves) != 3:
            stdio.write("ERROR: Invalid input format\n")
            continue

        # Extract row, column, and value from the input
        row, col, value = user_moves

        # Validate row and column indices
        if not (0 <= int(row) < height and 0 <= int(col) < width):
            stdio.write(f"ERROR: Field {row} {col} is out of bounds\n")
            continue

        # Validate the move
        validate_and_execute_move(row, col, value, state)


def validate_piece_type():
    """
    Validates the type of the game piece.

    Returns:
        None
    """
    allowed_pieces = {"d": True, "a": True, "c": True, "b": True}

    # Read the piece type from the user
    piece = stdio.readString().strip()

    if piece not in allowed_pieces:
        stdio.write(f"ERROR: Invalid piece type {piece}")
        exit()


def validate_item_size():
    """
    Validates the size of the game item.

    Returns:
        None
    """
    valid_item_styles = {"d": True, "l": True}
    valid_sizes = {1: True, 2: True}

    try:
        # Read item style and size from the user
        item_style = stdio.readString().strip()
        size_val = int(stdio.readString().strip())

        # Check if the item style is valid
        if item_style not in valid_item_styles:
            stdio.write(f"ERROR: Invalid item style {item_style}")
            exit()

        # Check if the size is valid
        if size_val not in valid_sizes:
            stdio.write(f"ERROR: Invalid item size {size_val}")
            exit()

        # For dark and light items, validate their specific sizes
        if item_style in valid_item_styles:
            if item_style == "d":
                if size_val not in (1, 2):
                    stdio.write(f"ERROR: Invalid size for dark item {size_val}")
                    exit()
            elif item_style == "l":
                if size_val not in (1, 2):
                    stdio.write(f"ERROR: Invalid size for light item {size_val}")
                    exit()

    except ValueError:
        # Handle the case where size cannot be converted to an integer
        stdio.write(f"ERROR: Invalid item size {size_val}")
        exit()


def check_object_type():
    """
    Checks if the provided object type is valid.

    Returns:
        bool: True if the object type is valid, False otherwise.
    """
    # Define valid object types
    valid_object_types = {'l', 'x', 'd', 's'}

    # Read the input character representing the object type
    input_char = stdio.readString().strip()

    # Check if the input character is a valid object type
    if input_char in valid_object_types:
        return True
    else:
        stdio.write(f"ERROR: Invalid object type {input_char}")
        exit()


def validate_piece_placement():
    """
    Validates the placement of a piece on the game board.
    """
    # Read inputs from the user
    input_char = stdio.readString().strip()
    input_a1 = stdio.readString().strip()
    input_a2 = stdio.readString().strip()
    input_a3 = stdio.readString().strip()
    input_rows = stdio.readInt()
    input_cols = stdio.readInt()

    # Validate the object type
    if input_char not in {'l', 'x', 'd', 's'}:
        stdio.write(f"ERROR: Invalid object type {input_char}")
        exit()

    try:
        # Convert dimensions to integers
        converted_a1 = int(input_a1)
        converted_a2 = int(input_a2)
        converted_a3 = int(input_a3)

        # Validate the coordinates
        if not (0 <= converted_a2 < input_rows) or not (0 <= converted_a3 < input_cols):
            stdio.write(f"ERROR: Field {converted_a2} {converted_a3} not on board")
            exit()

    except ValueError:
        stdio.write(f"ERROR: Invalid coordinates or dimensions")
        exit()

    # Validate the dimensions of the piece
    if input_char == 'd' and converted_a1 not in {1, 2}:
        stdio.write(f"ERROR: Invalid dimension for dark piece {converted_a1}")
        exit()
    elif input_char == 'l' and converted_a1 not in {1, 2}:
        stdio.write(f"ERROR: Invalid dimension for light piece {converted_a1}")
        exit()

    # Check constraints for placing the piece on the board
    process_and_validate_constraints(input_char, converted_a1, converted_a2, converted_a3, input_rows, input_cols)


def place_updated_sinks(placement_values):
    """
    Updates the game board with the locations of the sinks.

    Args:
        placement_values (list): The current state of the game board.
    """
    i = 0
    while i < len(sink_objects):
        sinking = sink_objects[i]
        data = sinking[0]
        row_index = sinking[2]
        col_index = sinking[3]

        if sinking[1] == 2:
            j = 0
            while j < 2:
                k = 0
                while k < 2:
                    placement_values[row_index + j][col_index + k] = data
                    k += 1
                j += 1
        else:
            placement_values[row_index][col_index] = data

        i += 1


def place_updated_blocked_elements(placement_values):
    """
    Updates the game board with the locations of the blocked elements.

    Args:
        placement_values (list): The current state of the game board.
    """
    index = 0
    while index < len(blocked_cells):
        element = blocked_cells[index]
        row_index, col_index = element[1], element[2]
        placement_values[row_index][col_index] = element[0]
        index += 1


def place_updated_dark_pieces(placement_values):
    """
    Updates the game board with the locations of the dark pieces.

    Args:
        placement_values (list): The current state of the game board.
    """
    index = 0
    while index < len(dark_pieces):
        d = dark_pieces[index]
        piece_type = d[1].upper()
        if d[1] not in ("a", "b", "c"):
            i = 0
            while i < 3:
                j = 0
                while j < 3:
                    placement_values[d[2] + i][d[3] + j] = d[2] * 10 + d[3]
                    j += 1
                i += 1
        else:
            placement_values[d[2]][d[3]] = piece_type
        index += 1

    
def place_updated_light_pieces(placement_values):
    """
    Updates the game board with the locations of the light pieces.

    Args:
        placement_values (list): The current state of the game board.
    """
    i = 0
    while i < len(light_pieces):
        lt = light_pieces[i]
        row_index, col_index = lt[2], lt[3]
        if lt[1] not in ("a", "b", "c"):
            j = row_index
            while j < row_index + 2:
                k = col_index
                while k < col_index + 2:
                    placement_values[j][k] = row_index * 10 + col_index
                    k += 1
                j += 1
        else:
            placement_values[row_index][col_index] = lt[1]
        i += 1

    
def review_updated_game_logic(placement_values, num_rows, num_cols, check):
    """
    Reviews the updated game logic by updating the board and either displaying it or processing player input.

    Args:
        placement_values (list): The current state of the game board.
        num_rows (int): The number of rows in the game board.
        num_cols (int): The number of columns in the game board.
        check (bool): A flag indicating whether to display the board (True) or process player input (False).
    """
    # Update the board with the placed values
    update_board(placement_values, num_rows, num_cols)

    # If check is True, display the board; otherwise, process player input
    if check:
        display_playboard(num_rows, num_cols, placement_values)
    else:
        process_user_input_and_validate(num_rows, num_cols, placement_values)


  
win_comparison = [0, 0]


def updated_print(num_rows, num_cols, placement_values):
    """
    Displays the game board and processes player input.

    Args:
        num_rows (int): The number of rows in the game board.
        num_cols (int): The number of columns in the game board.
        placement_values (list): The current state of the game board.
    """
    # Display the game board
    display_playboard(num_rows, num_cols, placement_values)

    # Process player input after displaying the board
    process_user_input_and_validate(num_rows, num_cols, placement_values)


def check_victory_condition(num_rows, num_cols, board_values):
    """
    Checks if there is a victory condition on the game board.

    Args:
        num_rows (int): The number of rows in the game board.
        num_cols (int): The number of columns in the game board.
        board_values (list): The current state of the game board.

    Returns:
        None
    """
    # Count the number of light and dark pieces on the board
    light_piece_count = sum(1 for row in board_values for cell in row if cell == 'l')
    dark_piece_count = sum(1 for row in board_values for cell in row if cell == 'd')

    # Check if either player has enough pieces to win
    if light_piece_count >= 4:
        display_playboard(num_rows, num_cols, board_values)
        stdio.write("Light wins!")
        exit()
    elif dark_piece_count >= 4:
        display_playboard(num_rows, num_cols, board_values)
        stdio.write("Dark wins!")
        exit()


def validate_and_execute_move(num_rows, num_cols, move_dir, board_values):
    """
    Validates and executes the player's move on the game board.

    Args:
        num_rows (int): The number of rows in the game board.
        num_cols (int): The number of columns in the game board.
        move_dir (str): The direction of the move ('l', 'u', 'r', 'd').
        board_values (list): The current state of the game board.

    Returns:
        None
    """
    # Get the current row and column index
    row_index, col_index = None, None
    for i in range(num_rows):
        for j in range(num_cols):
            if board_values[i][j].lower() == move_dir.lower():
                row_index, col_index = i, j
                break
        if row_index is not None:
            break

    if row_index is None or col_index is None:
        stdio.write(f"ERROR: Invalid move {move_dir}")
        exit()

    # Perform the move based on the direction
    if move_dir.strip().lower() == "l":
        col_index -= 1
    elif move_dir.strip().lower() == "u":
        row_index += 1
    elif move_dir.strip().lower() == "r":
        col_index += 1
    elif move_dir.strip().lower() == "d":
        row_index -= 1
    else:
        stdio.write(f"ERROR: Invalid direction {move_dir}")
        exit()

    # Check if the move is valid
    if not (0 <= row_index < num_rows and 0 <= col_index < num_cols):
        stdio.write(f"ERROR: Field {row_index} {col_index} not on board")
        exit()
    elif board_values[row_index][col_index].strip() != "":
        stdio.write(f"ERROR: Field {row_index} {col_index} not free")
        exit()

    # Update the board values after the move
    board_values[row_index][col_index] = move_dir.lower()

    # Check for player win
    check_victory_condition(num_rows, num_cols, board_values)

    # Print the board after the move
    updated_print(num_rows, num_cols, board_values)


checker_increment = [0]


def execute_user_move(curr_row, curr_col, move_dir, board_values):
    """
    Executes the user's move on the game board.

    Args:
        curr_row (int): Current row index of the piece.
        curr_col (int): Current column index of the piece.
        move_dir (str): Direction of the move ('l', 'u', 'r', 'd').
        board_values (list): Current state of the game board.

    Returns:
        None
    """
    # Check if the move direction is valid
    if move_dir.strip() not in player_directions:
        stdio.write(f"ERROR: Invalid direction {move_dir}")
        exit()

    # Define the bounds for rows and columns
    min_row, max_row = 0, 10
    min_col, max_col = 0, 10

    # Determine the new position based on the move
    new_row, new_col = curr_row, curr_col
    if move_dir.strip() == "l":
        new_col -= 1
    elif move_dir.strip() == "u":
        new_row += 1
    elif move_dir.strip() == "r":
        new_col += 1
    elif move_dir.strip() == "d":
        new_row -= 1

    # Check if the new position is within the board's bounds
    if not (min_row <= new_row < max_row and min_col <= new_col < max_col):
        stdio.write(f'ERROR: Cannot move beyond the board')
        exit()

    # Check if the piece is being moved to the starting position (3, 3)
    if new_row == 3 and new_col == 3 and board_values[curr_row][curr_col] == 'a':
        stdio.write(f'ERROR: Piece cannot be returned to starting position')
        exit()

    # Perform the move by updating the board values
    board_values[new_row][new_col] = board_values[curr_row][curr_col]
    board_values[curr_row][curr_col] = ' '

    # Call the print function to display the updated board
    updated_print(10, 10, board_values)


def verify_second_move_availability(curr_row, curr_col, move_dir, game_board):
    """
    Verifies the availability of the second move and executes it if valid.

    Args:
        curr_row (int): Current row index of the piece.
        curr_col (int): Current column index of the piece.
        move_dir (str): Direction of the move ('l', 'u', 'r', 'd').
        game_board (list): Current state of the game board.

    Returns:
        None
    """
    if move_dir == 'r':
        piece_type = game_board[curr_row][curr_col]
        if piece_type == 'd' and game_board[curr_row][curr_col + 1] == 44:
            stdio.write("ERROR: Cannot move a 2x2x2 piece on the second move")
            exit()
    validate_and_execute_move(curr_row, curr_col, move_dir, game_board)


def validate_player_moves(row_idx, col_idx, player_move, board_state):
    """
    Validates the moves made by the player.

    Args:
        row_idx (int): Row index of the piece.
        col_idx (int): Column index of the piece.
        player_move (str): Direction of the player's move.
        board_state (list): Current state of the game board.

    Returns:
        None
    """
    # Convert coordinates to integers
    row_idx, col_idx = int(row_idx), int(col_idx)

    # Check if it's the first move and if the piece belongs to the correct player
    if checker_increment[0] == 0:
        if str(board_state[row_idx][col_idx]).isupper():
            stdio.write(f"ERROR: Piece does not belong to the correct player")
            exit()
        elif not player_move:
            stdio.write("Light loses")
            exit()

    # Increment the checker increment
    checker_increment[0] += 10

    # Check if there is a piece at the specified coordinates
    if board_state[row_idx][col_idx] == ' ':
        stdio.write(f'ERROR: No piece on field {row_idx} {col_idx}')
        exit()

    # Check the validity of the move
    verify_second_move_availability(row_idx, col_idx, player_move, board_state)

        
# driver code
def start_game():
    num_args = len(sys.argv)
    expected_args = 4

    if num_args != expected_args:
        stdio.write(f"ERROR: Expected {expected_args} arguments, received {num_args}\n")
        exit()

    try:
        rows_count = int(sys.argv[1])
        cols_count = int(sys.argv[2])
        mode = int(sys.argv[3])
    except ValueError:
        stdio.write("ERROR: Invalid arguments\n")
        exit()

    if not (8 <= rows_count <= 10) or not (8 <= cols_count <= 10) or not (0 <= mode <= 1):
        stdio.write("ERROR: Invalid game settings\n")
        exit()

    process_user_input_and_validate(rows_count, cols_count, mode)


# Main function
if __name__ == '__main__':
    start_game()
