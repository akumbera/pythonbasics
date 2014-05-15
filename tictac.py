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
	pass

def new_game():
	game_state.board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	game_state.game_over=False

def quit_game():
	game_state.game_over=True
	print 'Thank you for playing.'

class game_state():
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	xturn = True
	game_over = False

def run_game():
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

run_game()