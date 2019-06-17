'''
Milestone 1 
Tic Tac Toe Came
'''

import random

 
def display_board(board):
	print("\n"*100)

	print("   |   |   ")
	print(" " + board[7] + " | " + board[8] + " | " + board[9])
	print("   |   |   ")
	print("--- --- ---")
	print("   |   |   ")
	print(" " + board[4] + " | " + board[5] + " | " + board[6])
	print("   |   |   ")
	print("--- --- ---")
	print("   |   |   ")
	print(" " + board[1] + " | " + board[2] + " | " + board[3])
	print("   |   |   ")


def player_input():
	marker = ""

	while not (marker == "X" or marker == "O"):
		marker = input("Player 1: Do you want to be X or O? ").upper()

	if marker == "X":
		return ("X", "O")
	else: 
		return ("O", "X")

def place_marker(board, marker, position):
	board[position] = marker


def win_check(board, mark):
	
	mark = mark.upper()

	return ((mark == board[1] and mark == board[2] and mark == board[3]) or 
	(mark == board[4] and mark == board[5] and mark == board[6]) or 
	(mark == board[7] and mark == board[8] and mark == board[9]) or 
	(mark == board[7] and mark == board[4] and mark == board[1]) or 
	(mark == board[8] and mark == board[5] and mark == board[2]) or 
	(mark == board[9] and mark == board[6] and mark == board[3]) or 
	(mark == board[7] and mark == board[5] and mark == board[3]) or 
	(mark == board[1] and mark == board[5] and mark == board[9]))

def choose_first():
	num = random.randint(1,2)
	player_first =  "Player {}".format(num)
	return player_first

def space_check(board, position):
	return board[position] ==  ''

def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True

def player_choice(board):
	
	position = 0

	while position not in [1,2,3,4,5,6,7,8,8] or not space_check(board, position):
		position = int(input("Please enter a number for your board position: "))

	return position

def replay():
	replay = input("Do you want to play again? Y/N: ").lower()

	if replay == "y" or replay == "yes":
		return True
	else: 
		print("Thanks for playing, see you next time") 

print("Welcome to Tic Tac Toe!")

while True:
	# Set the game up here
	theBoard = ['']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + " will go first.")


	play_game = input("Are you ready to play the game? (Y/N)").lower()
	if play_game[0] == "y":
		game_on = True
	else:
		game_on = False


	while game_on:
		if turn == "Player 1":

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)

			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print("Congratulations! You have won the game!")
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print("The game is a draw!")
					break
				else:
					turn = "Player 2"

		else:

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)

			if win_check(theBoard, player2_marker):
				display_board(theBoard)
				print("Congratulations! You have won the game!")
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print("The game is a draw!")
					break
				else:
					turn = "Player 1"

	if not replay():
		break



