

def piecewise_sum(a, b):
	'''Return the piecewise sum of two twoples'''
	return (a[0] + b[0], a[1] + b[1])


def find_path(coords, board, dir):
	'''Return possible squares of a piece'''
	rank, file = coords
	piece = board[rank][file][1]
	possible_squares = []
	check = True
	check_tile = coords
	
	while check:
		
		possible_squares += [check_tile]
		# Make sure check_tile isn't out of bounds or return current movelist
		check_tile = piecewise_sum(check_tile, dir)
		if any((max(check_tile) > 7, min(check_tile) < 0)):
			return possible_squares

		side_check = board[check_tile[0]][check_tile[1]][1]["side"]
		
		if side_check != "n":
			check = False
			if piece["side"] != side_check:
				possible_squares += [check_tile]
				
	return possible_squares


def cardinal(coords, board):
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	moveset = []
	
	for dir in directions:
		moveset += find_path(coords, board, dir)
		
	return moveset

def diagonal(coords, board):
	directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
	moveset = []
	
	for dir in directions:
		moveset += find_path(coords, board, dir)
		
	return moveset


def pawn(coords, board):
	rank, file = coords
	piece = board[rank][file][1]
	moveset = []

	if piece["side"] == "w":
		dir = 1
	elif piece["side"] == "b":
		dir = -1
	
	if file == 0:
		check_files = [1]
	elif file == 7:
		check_files = [6]
	else:
		check_files = (file -	1, file + 1)
	
	for poss in check_files:
		dest_piece = board[rank + dir][poss][1]["side"]
		if dest_piece != "n" and piece["side"] != dest_piece:
			moveset += [(rank + dir, poss)]
	
	front_piece = board[rank + dir][file][1]
	if front_piece["side"] == "n":
		moveset += [(rank + dir, file)]
		if piece["counter"] == 0:
			double_space = board[rank + 2 * dir][file][1]
			if double_space["side"] == "n":
				moveset += [(rank + 2 * dir, file)]
		
	return moveset


def possible_moveset(coords, board, side):
	rank, file = coords
	piece = board[rank][file][1]
	start = [(rank, file)]
	
	if piece["side"] != side:
		return moveset
	
	if piece["type"] == "p":
		return start + pawn(coords, board)
	
	if piece["type"] == "b":
		return start + diagonal(coords, board)
	
	if piece["type"] == "R":
		return start + cardinal(coords, board)
	
	if piece["type"] == "Q":
		return start + diagonal(coords, board) + cardinal(coords, board)


#Gets opponents moveset
def opponent_moves(board, turn):
	opponent_side = [side != turn for side in list("wb")][0]
	moveset = []
	
	for rank in range(8):
		for file in range(8):
			if board[rank][file][1]["side"] == opponent_side:
				moveset += possible_moveset((rank, file), board, turn)
	
	return moveset


#Moveset with potential hard pins considered

