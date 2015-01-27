from random import randint

game_board = {
'Go':0,
'Mediterranean Avenue':0,
'Community Chest 1':0,
'Baltic Avenue':0,
'Income Tax':0,
'Reading Railroad':0,
'Oriental Avenue':0,
'Chance 1':0,
'Vermont Avenue':0,
'Connecticut Avenue':0,
'Jail':0,
'Saint Charles Place':0,
'Electric Company':0,
'States Avenue':0,
'Virginia Avenue':0,
'Pennsylvania Railroad':0,
'Saint James Place':0,
'Community Chest 2':0,
'Tennessee Avenue':0,
'New York Avenue':0,
'Free Parking':0,
'Kentucky Avenue':0,
'Chance 2':0,
'Indiana Avenue':0,
'Illinois Avenue':0,
'B and O Railroad':0,
'Atlantic Avenue':0,
'Ventnor Avenue':0,
'Water Works':0,
'Marvin Gardens':0,
'Goto Jail':0,
'Pacific Avenue':0,
'North Carolina Avenue':0,
'Community Chest 3':0,
'Pennsylvania Avenue':0,
'Short Line':0,
'Chance 3':0,
'Park Place':0,
'Luxury Tax':0,
'Boardwalk':0
}

class Pawn(object):
	'''Defines the player's piece.'''

	def __init__(self):
		self.position = 0;
		#in_jail = False;
		#when 3 doubles are rolled in a row, piece is sent to jail
		self.doubles_last_turn = False;
		self.doubles_counter = 0;

	def roll_dice(self):
		a = randint(1,6);
		b = randint(1,6);

		if a == b:
			self.doubles_counter += 1;
			self.doubles_last_turn = True;

		result = a + b;
		return result;

	def draw_chance(self):
		chance = randint(1,16);
		if chance == 1:
			#go to jail
			self.position = 10;
			self.increment_position(self.position);
		elif chance == 2:
			#go to go
			self.position = 0;
			self.increment_position(self.position);
		elif chance == 3:
			#go to illinois ave
			self.position = 24;
			self.increment_position(self.position);
		elif chance == 4:
			#go to st charles place
			self.position = 11;
			self.increment_position(self.position);
		#chance cards can also move you to the nearest railroad or utility.
		#maybe in another version.

	def draw_cc(self):
		chest = randint(1,17);
		if chest == 1:
			#go to jail
			self.position = 10;
			self.increment_position(self.position);
		elif chest == 2:
			#go to go
			self.position = 0;
			self.increment_position(self.position);

	def increment_position(self, location):
		#dict.keys()[integer] returns the key in that location, in this case a string.
		#I think this is tenchnically whrong, since dicts in python are
		#supposed to be unordered. I don't think this changes anything, though.
		game_board[game_board.keys()[location]] += 1;


	def move(self):
		#Roll the dice
		result = self.roll_dice();

		#Check to see if the piece has rolled 3 doubles in a row
		if self.doubles_counter==3:
			self.position = 10;
			self.doubles_counter = 0;
			self.doubles_last_turn = False;
			self.increment_position(self.position);
		else:
			#Update position on the board
			self.position = (self.position + result)%40;
			self.increment_position(self.position);

			#Draw community chest card
			if self.position==2 or self.position==17 or self.position==33:
				self.draw_cc();
				
			#Draw chance card
			elif self.position==7 or self.position==22 or self.position==36:
				self.draw_chance();

			#Check to see if doubles were thrown last turn. If not, exit.
			else:
				if self.doubles_last_turn == True:
					self.doubles_last_turn == False;
					self.move();
				else:
					self.doubles_counter = 0;
					return;

simulate = True;

while simulate==True:

	#Create a new instance of the pawn class
	battleship = Pawn();

	user_input = raw_input('How many dice rolls should the piece move? ');
	sample_size = int(user_input);

	for x in range(sample_size):
		battleship.move();
	print(game_board);
	simulate = False;