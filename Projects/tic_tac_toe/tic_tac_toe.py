from utils import *


def tic_tac_toe():
    turn_counter = 0
    game_status = 'new'
    player_one = ''
    player_two = ''
    current_player = ''
    board = []

    while True:
        match game_status:
            case 'new':
                turn_counter = 0
                user_input = input(
                    'Would you like to start a new game?(y/n)\n').lower()
                if (user_input == 'y'):
                    game_status = 'ongoing'
                    player_one = input('Enter a name for player one:\n')
                    player_two = input('Enter a name for player two:\n')
                    current_player = player_one
                    user_input = input(
                    'Would you like to see shortcuts for board placement?(y/n)\n').lower()
                    if(user_input == 'y'):
                        print_shortcuts()
                    board = reset_board()
                    print(
                        f'{player_one} will go first and be X!\n'
                        'New board created: '
                    )
                elif (user_input == 'n'):
                    print('Come back and play again.')
                    return
                else:
                    print('Please enter a valid input')
            case 'ongoing':
                symbol = 'X' if current_player == player_one else 'O'
                print(f'{current_player}\'s turn:')
                placement = input(f'Enter where you would like to place {symbol}:\n').lower()
                board = place_symbol_on_board(symbol, board, placement)
                # We need to check if a user has won
                if (check_for_win(board, placement)):
                    game_status = 'new'
                    print(f'{current_player} won!!')
                else:
                    current_player = player_one if current_player == player_two else player_two
                    turn_counter= turn_counter + 1
                    print(f'counter: {turn_counter}')
                    if(turn_counter >= 9):
                        game_status = 'new'
                        print('It\'s a draw!')

        print(serialize_board(board))


tic_tac_toe()
