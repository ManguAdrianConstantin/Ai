from random import randrange, random
from time import sleep
print("Made by Mangu Adrian-Constantin")
#First, setup the board!!

def draw_board():
    print '', board[1], '|', board[2], '|', board[3], \
          '\n-----------\n', \
          '', board[4], '|', board[5], '|', board[6], \
          '\n-----------\n', \
          '', board[7], '|', board[8], '|', board[9], \
          '\n'
#Next, Choose what team you're on!

def player_team():
    team = raw_input('Do you want to be X or O? \n').upper()
    print
    if team == 'X':
        return ['X', 'O']
    elif team == 'O':
        return ['O', 'X']
    else:
        print ('That is not a valid choice. Please try again \n')
        return player_team()
#Next, Find out what player goes first!

def first_turn():
    turn = random()
    if turn <= .494:
        print 'You will go first \n'
        return ('user', True)
    else:
        print 'The Computer will go first \n'
        return ('computer', False)
#Next, be able to determine which spaces are available!

def available(space):
    if board[space] == ' ':
        return True
#Next, allow a player to pick their move!

def user_turn():
    try:
        move = int(raw_input('Where would you like to move? (Enter a number from 1-9) \n'))
        if 0 < move < 10:
            if not available(move):
                print ('That space is already taken by a player. '
                       'Please select an open space \n')
                return user_turn()
            else:
                board[move] = user_team
                print
    except:
        print 'That is not a valid move. Please try again. \n'
        return user_turn()   
#Now define the A.I!

def computer_turn():
    move = randrange(1, 10)
    if available(move):
        board[move] = computer_team
        return move
    else:
        return computer_turn()
#Next, we must check if the game has ended or not, and see who won!

def end_game():
    for row in range(1, 10, 3):
        if not available(row):
            if board[row] == board[row + 1] and board[row] == board[row + 2]:
                return True
    for column in range(1, 4):
        if not available(column):
            if board[column]== board[column + 3] and board[column] == board[column + 6]:
                return True
    for diagonal in range(1, 10, 2):
        if not available(diagonal):
            if (diagonal == 1 and board[diagonal] == board[diagonal + 4]
                and board[diagonal] == board[diagonal + 8]):
                return True
            elif (diagonal == 3 and board[diagonal] == board[diagonal + 2]
                and board[diagonal] == board[diagonal + 4]):
                return True
    if board.count('X') + board.count('O') == 9:
        return 'Tie'

def check_winner():
    global user_win, computer_win, ties
    if end_game() == 'Tie':
        ties += 1
        draw_board()
        print ("The game is a tie. You're going to have to try harder"
               "\nif you wish to beat the computer! \n")
    elif end_game():
        if turn == 'user':
            user_win += 1
            draw_board()
            print ('You won! \n')
        else:
            computer_win += 1
            draw_board()
            print ('The computer has won! But... We already knew'
                   'that would happen. (: \n')    
#Finally, give the option of a New Game+!

def play_again():
    print 'Your wins:', user_win, '\n' \
          'Computer wins:', computer_win, '\n' \
          'Ties:', ties, '\n'
    restart = raw_input('Do you wish to play another game? Yes or no? \n').upper()
    print
    if restart == 'YES':
        return True
    elif restart == 'NO':
        return False
    else:
        print ('That is not a valid choice. Please try again. \n')
        return play_again()
#Main Program:    

print ('Welcome to my Impossible Tic-Tac-Toe game! You are of the bravest'
       'of souls \nto take on my challenge, but only failure awaits you. \n')
count = 1
user_win, computer_win, ties = 0, 0, 0
new_game = True
while new_game:
    board = [' '] * 10
    user_team, computer_team = player_team()
    turn, strategy = first_turn()
    print 'Game', count, '\n'
    while not end_game():
        if turn == 'user':
            draw_board()
            user_turn()
            check_winner()
            turn = 'computer'
        else:
            draw_board()
            print 'The computer is thinking... \n'
            sleep(1)
            space_taken = computer_turn()
            print 'The computer moved on space', space_taken, '\n'
            check_winner()
            turn = 'user'
    if not play_again():
        new_game = False
    count += 1
