def draw_board(state):
	print state[0] + '|' + state[1] + '|' + state[2]
	print '------'
	print state[3] + '|' + state[4] + '|' + state[5]
	print '------'
	print state[6] + '|' + state[7] + '|' + state[8]

def input_board(y):
	if game_state.xturn==True:
		game_state.board[y]='X'
		game_state.xturn=False
	else:
		game_state.board[y]='O'
		game_state.xturn=True

def check_victory():
	if game_state.board[0] != ' ' and game_state.board[0] == game_state.board[1] == game_state.board[2]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[0] != ' ' and game_state.board[0] == game_state.board[3] == game_state.board[6]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[0] != ' ' and game_state.board[0] == game_state.board[4] == game_state.board[8]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[1] != ' ' and game_state.board[1] == game_state.board[4] == game_state.board[7]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[2] != ' ' and game_state.board[2] == game_state.board[5] == game_state.board[8]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[3] != ' ' and game_state.board[3] == game_state.board[4] == game_state.board[5]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[6] != ' ' and game_state.board[6] == game_state.board[7] == game_state.board[8]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[6] != ' ' and game_state.board[6] == game_state.board[4] == game_state.board[2]:
		print 'Player '+game_state.board[0]+' wins!'
		choose_new_game()
	elif game_state.board[0] != ' ' and game_state.board[1] != ' ' and game_state.board[2] != ' ' and game_state.board[3] != ' ' and game_state.board[4] != ' ' and game_state.board[5] != ' ' and game_state.board[6] != ' ' and game_state.board[7] != ' ' and game_state.board[8] != ' ':
		print 'Stalemate!'
		choose_new_game()
	else:
		pass

def choose_new_game():
	s = raw_input('Would you like to play again? (yes/no) ')
	if s=='Yes' or s=='yes' or s=='y':
		new_game()
	elif s=='No' or s=='no' or s=='n':
		quit_game()
	else:
		print 'Error: Please enter yes or no'
		choose_new_game()

def new_game():
	game_state.board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	game_state.game_over=False
	game_state.xturn=True
	run_game()

def quit_game():
	game_state.game_over=True
	print 'Thank you for playing.'

class game_state():
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	xturn = True
	game_over = False

def welcome():
	locationmap=['0','1','2','3','4','5','6','7','8']
	print 'Welcome to tic-tac-toe! Enter numbers 0-8 to place a piece on that location. Enter 9 to quit.'
	draw_board(locationmap)
	print 'X goes first. Have fun!'

def run_game():
	draw_board(game_state.board)
	while game_state.game_over==False:
		s = int(raw_input('Please select a location: '))
		if s==0 or s==1 or s==2 or s==3 or s==4 or s==5 or s==6 or s==7 or s==8:
			if game_state.board[s]==' ':
				input_board(s)
				draw_board(game_state.board)
				check_victory()
			else:
				print 'Error: location not empty.'
		elif s==9:
			quit_game()
		else:
			print 'Please enter a valid command.'

welcome()
run_game()