def place_symbol_on_board(symbol, board, placement):
    turn_ongoing = True
    while turn_ongoing:
        match placement:
            case 'top left' | 'tl':
                board[0][0] = symbol
                turn_ongoing = False
            case 'top middle' | 'tm':
                board[0][1] = symbol
                turn_ongoing = False
            case 'top right' | 'tr':
                board[0][2] = symbol
                turn_ongoing = False
            case 'middle left' | 'ml':
                board[1][0] = symbol
                turn_ongoing = False
            case 'middle' | 'm':
                board[1][1] = symbol
                turn_ongoing = False
            case 'middle right' | 'mr':
                board[1][2] = symbol
                turn_ongoing = False
            case 'bottom left' | 'bl':
                board[2][0] = symbol
                turn_ongoing = False
            case 'bottom middle' | 'bm':
                board[2][1] = symbol
                turn_ongoing = False
            case 'bottom right' | 'br':
                board[2][2] = symbol
                turn_ongoing = False
            case _:
                user_input = input(f'Looks like you entered a wrong input. Would you like to see placement shortcuts?(y/n)\n').lower()
                if(user_input == 'y'):
                    print_shortcuts()
                placement = input(f'Please enter a correct placement input:\n').lower()
    return board

def reset_board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def serialize_board(board):
    serialized_board = (
        f'{board[0][0]}|{board[0][1]}|{board[0][2]}\n'
        f'{board[1][0]}|{board[1][1]}|{board[1][2]}\n'
        f'{board[2][0]}|{board[2][1]}|{board[2][2]}'
    )
    return serialized_board

def print_shortcuts ():
    print(
        'Here are the shortcuts for placements on the board.\n'
        'top left => tl\n'
        'top middle => tm\n'
        'top right => tr\n'
        'middle left => ml\n'
        'middle => m\n'
        'middle right => mr\n'
        'bottom left => bl\n'
        'bottom middle => bm\n'
        'bottom right => br\n'
    )


def check_for_win(board, placement):
    match placement:
        case 'top left' | 'tl':
            if (
                board[0][0] == board[0][1] == board[0][2] != ' ' or
                board[0][0] == board[1][1] == board[2][2] != ' ' or
                board[0][0] == board[1][0] == board[2][0] != ' '
            ):
                return True
        case 'top middle' | 'tm':
            if (
                board[0][0] == board[0][1] == board[0][2] != ' ' or
                board[0][1] == board[1][1] == board[2][1] != ' '
            ):
                return True
        case 'top right' | 'tr':
            if (
                board[0][0] == board[0][1] == board[0][2] != ' ' or
                board[0][2] == board[1][1] == board[2][0] != ' ' or
                board[0][2] == board[1][2] == board[2][2] != ' '
            ):
                return True
        case 'middle left' | 'ml':
            if (
                board[1][0] == board[1][1] == board[1][2] != ' ' or
                board[0][0] == board[1][0] == board[2][0] != ' '
            ):
                return True
        case 'middle' | 'm':
            if (
                board[1][0] == board[1][1] == board[1][2] != ' ' or
                board[0][1] == board[1][1] == board[2][1] != ' '
            ):
                return True
        case 'middle right' | 'mr':
            if (
                board[1][0] == board[1][1] == board[1][2] != ' ' or
                board[0][2] == board[1][2] == board[2][2] != ' '
            ):
                return True
        case 'bottom left' | 'bl':
            if (
                board[2][0] == board[1][0] == board[0][0] != ' ' or
                board[2][0] == board[1][1] == board[0][2] != ' ' or
                board[2][0] == board[2][1] == board[2][2] != ' '
            ):
                return True
        case 'bottom middle' | 'bm':
            if (
                board[2][0] == board[2][1] == board[2][2] != ' ' or
                board[2][1] == board[1][1] == board[0][1] != ' '
            ):
                return True
        case 'bottom right' | 'br':
            if (
                board[2][2] == board[1][2] == board[0][2] != ' ' or
                board[0][0] == board[1][1] == board[2][2] != ' ' or
                board[2][0] == board[2][1] == board[2][2] != ' '
            ):
                return True

    return False
