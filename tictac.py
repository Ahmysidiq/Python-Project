import random
print("Hello what shall we call you, type a nickname to begin the game or hit ctrl + c to quit")
name = input(" ")


print ("[+] Welcome "+ name + " to a peaceful game of X and O to determine who is the goat, you win, Messi is the GOAT, you lose, Ronaldo is the GOAT. [+]")


print("Hit your letter to have a deal or any other button to back out")
player_card = input("") 
player_card = player_card.upper()
if player_card.upper() in ("X", "O") :
	print("welcome to the Gulak " + name)
else:
	print("You sire are a coward, " + name) 
	
if player_card.upper ()== "X":
	AI = "O"
else:
	AI = "X"
print(AI)

board = [" "," "," ",
	 " "," "," ",
	 " "," "," "]
	 
def play_board(board):
	print(f" {board[0]} | {board[1]} | {board[2]}")
	print("-----------")
	print(f" {board[3]} | {board[4]} | {board[5]}")
	print("-----------")
	print(f" {board[6]} | {board[7]} | {board[8]}")
	

def in_game():
	while True:
		print("Pick a board number to start the game, choose from numbers (1-9) ")
		game_number = input("> ")
				
		if not game_number.isdigit():
			print("invalid input fool, enter a proper digit")
			continue
		game_number = int(game_number)
				
		if game_number < 1 or game_number > 9:
			print(" The number is still invalid you fool, are you even mad, fucking enter a proper number from 1-9")
			continue
		
		return game_number

while " " in board:
	play_board(board)
	move = in_game() - 1
	if board[move] == " ":
		board[move] = player_card
	else:
		print("Spot taken, are you fucking blind man")
		continue
	empty_spots = []
	for i in range(9):
		if board[i] == " ":
			empty_spots.append(i)
	ai_move = random.choice(empty_spots)
	board[ai_move] = AI
	wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
		
	def check_win(board, player):
		
		for a, b, c in wins:
			
			if board[a] == board[b] == board[c] == player:
				return True
		return False	
	if check_win(board, player_card):
		print("You win - *")
		break
	if check_win(board, AI):
		print("AI wins")
		break
	if " " not in board:
		print(" It is a draw")
		break
		
play_board(board)
