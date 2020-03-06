import numpy as np


#This function will return the constants which decide the spacing of the board
def give_tile_location(coords, size, t_lth):
	coords, ones, dim = (np.array(coords[::-1]), np.ones(2), np.array(size))
	board_origin = 1 / 2 * (dim - 7 * t_lth * ones)
	position = board_origin + t_lth * ones * coords
	return tuple(position)

