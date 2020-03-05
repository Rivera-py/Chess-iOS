from scene import *
from ui import Path
#Importing starting positions
from new_game import current_board, is_select
from board_spacing import give_tile_location


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
		#Below decides whether there is a piece and it's info
		if self.piece["type"] == "p":
			self.position_chg = -0.05
		else:
			self.position_chg = -0.2
		if piece["side"] == None:
			pass
		elif self.piece["side"] == "w":
			self.marker = LabelNode(piece["type"],('Academy Engraved LET', t_lth), color='white', position=(0, t_lth * self.position_chg))
			self.add_child(self.marker)
		elif self.piece["side"] == "b":
			self.marker = LabelNode(piece["type"],('Academy Engraved LET', t_lth), color='black', position=(0, t_lth * self.position_chg))
			self.add_child(self.marker)
		#Decides whether the square lights up or not (during move selection)
		if self.light == True:
			self.light_square = ShapeNode(square, "#2f77ff", "#300cdd", position = (0,0), alpha = 0.3)
			self.add_child(self.light_square)


#The root node
class Board (Scene):
	def setup(self):
		#The global variable deciding the size of each tile
		global t_lth
		self.background_color = '#7d07c1'
		t_lth = 3 / 40 * self.size.y
		#Instantiating each tile
		for rank in range(8):
			for file in range(8):
				cell_coords, cell_piece, cell_light = current_board[rank][file]
				cell = Tile(cell_coords, give_tile_location(cell_coords, self.size, t_lth), cell_piece, cell_light)
				self.add_child(cell)


run(Board(), PORTRAIT)
