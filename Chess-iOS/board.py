from scene import *
from ui import Path
#Importing starting positions
from new_game import new_game


#This class will be called for each tile
class Tile (ShapeNode):
	#Args will be board coords (x, y) s.t. 0 <= x, y <= 7
	#and a dictionary containing piece info
	def __init__(self, coords, piece):
		square = Path.rect(0, 0, t_lth, t_lth)
		centre = (x_0 + coords[0] * t_lth, y_0 + coords[1] * t_lth)
		#Creates lattice effect
		if sum(coords) % 2 == 0:
			tile_colour = '#3e3e3e'
		else:
			tile_colour = '#d3d3d3'
		#Creates square
		ShapeNode.__init__(self, square, tile_colour, '#adadad', position=centre)
		self.piece = piece
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


#The root node
class Board (Scene):
	def setup(self):
		#The global variables deciding the size of each tile
		global b_lth, t_lth, x_0, y_0
		self.background_color = '#7d07c1'
		b_lth = self.size.y * 0.6
		t_lth = b_lth / 8
		x_0 = self.size.x / 2 - b_lth / 2 + t_lth / 2
		y_0 = self.size.y / 2 - b_lth / 2 + t_lth / 2
		#Instantiating each tile
		for tile in new_game:
			self.cell = Tile(tile[0], tile[1])
			self.add_child(self.cell)

run(Board(), PORTRAIT)
