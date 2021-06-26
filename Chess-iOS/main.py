from scene import *
from ui import Path
from new_game import current_board, is_select, empty, selected_coords
from board_spacing import give_tile_location
from move_functions import possible_moveset
from copy import deepcopy


#This class will be called for each tile
class Tile (ShapeNode):
	#Args will be board coords (x, y) s.t. 0 <= x, y <= 7
	def __init__(self, coords, location, piece, light):
		self.coords = coords
		self.location = location
		self.piece = piece
		self.light = light
		square = Path.rect(0, 0, t_lth, t_lth)
		
		#Creates lattice effect
		if sum(coords) % 2 == 0:
			tile_colour = '#3e3e3e'
		else:
			tile_colour = '#d3d3d3'
			
		#Creates square
		ShapeNode.__init__(self, square, tile_colour, '#adadad', position=location)
		
		#Below decides whether there is a piece and its info
		if self.piece["type"] == "p":
			self.position_chg = -0.05
		else:
			self.position_chg = -0.2
			
		if piece["side"] == "n":
			pass
			
		elif self.piece["side"] == "w":
			self.marker = LabelNode(
				piece["type"],
				('Academy Engraved LET', t_lth), 
				color='white', 
				position=(0, t_lth * self.position_chg))
			self.add_child(self.marker)
			
		elif self.piece["side"] == "b":
			self.marker = LabelNode(
				piece["type"],
				('Academy Engraved LET', t_lth), 
				color='black', 
				position=(0, t_lth * self.position_chg)
			)
			self.add_child(self.marker)
			
		#Decides whether the square lights up or not (during move selection)
		if self.light == True:
			self.light_square = ShapeNode(
				square, 
				"#2f77ff", 
				"#300cdd", 
				position = (0,0), 
				alpha = 0.3
			)
			self.add_child(self.light_square)


#The root node
class Board (Scene):
	def setup(self):
		#The global variable deciding the size of each tile
		global t_lth
		
		self.background_color = '#7d07c1'
		t_lth = 3 / 40 * self.size.y
		#Cycles the turn
		self.turns = ("w", "b")
		self.turn_counter = 0
		self.turn = self.turns[0]
		#Creates initial board
		self.update_board()
	
	
	#Instantiating each tile
	def update_board(self):
		for cell in self.children:
			cell.remove_from_parent()
			
		for rank in range(8):
			for file in range(8):
				cell_coords, cell_piece, cell_light = current_board[rank][file]
				cell = Tile(
					cell_coords, give_tile_location(cell_coords, self.size, t_lth), 
					cell_piece, 
					cell_light
				)
				self.add_child(cell)
	
	
	def lights_off(self):
		for rank in range(8):
			for file in range(8):
				current_board[rank][file][2] = False
	
	
	#Changes board info according to a moving piece
	def move_piece(self, pt_1, pt_2):
		current_board[pt_2[0]][pt_2[1]][1] = deepcopy(current_board[pt_1[0]][pt_1[1]][1])
		current_board[pt_2[0]][pt_2[1]][1]["counter"] += 1
		current_board[pt_1[0]][pt_1[1]][1] = empty
		
	
	def touch_began(self, touch):
		global side, is_select, selected_coords
		for cell in self.children:
			if cell.frame.contains_point(touch.location):
				coords = cell.coords
		
		#Selects a piece
		if is_select == False:
			
			if len(possible_moveset(coords, current_board, self.turn)) > 1:
				for index in possible_moveset(coords, current_board, self.turn):
					current_board[index[0]][index[1]][2] = True
				self.update_board()
				is_select = True
				self.selected_coords = coords
		
		#Either moves or deselects a piece
		elif is_select == True:
			
			if coords in possible_moveset(self.selected_coords, current_board, self.turn) and coords != self.selected_coords:
				self.move_piece(self.selected_coords, coords)
				self.turn_counter += 1
				self.lights_off()
				is_select = False
				self.turn = self.turns[self.turn_counter % 2]
			else:
				self.lights_off()
				is_select = False
			self.update_board()


run(Board(), PORTRAIT)
