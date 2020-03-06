

def possible_moveset(coords, board, turn):
	rank, file = coords
	piece = board[rank][file][1]
	moveset = [(rank, file)]
	
	if piece["side"] != turn:
		return moveset
	
	if piece["type"] == "p":
		
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
