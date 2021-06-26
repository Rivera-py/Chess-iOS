rk_0 = 'RkbQKbkR'
rk_7 = 'RkbQKbkR'
empty = {"side": "n", "type": ""}

'''
A rank here is a list of squares in its row.

Each square is a list of elements:
	- Tuple with board coordinates.
	- Dict with:
		- side (w or b)
		- type (piece type)
		- counter (times moved)
	- Boolean of whether piece is selected by player.
'''

rank_0 = [[(0, file), {"side": "w", "type": rk_0[file], "counter" : 0}, False] for file in range(8)]
rank_1 = [[(1, file), {"side": "w", "type" : "p", "counter" : 0}, False] for file in range(8)]
ranks_2_5 = [[[(rank, file) , empty, False] for file in range(8)] for rank in range(2, 6)]
rank_6 = [[(6, file), {"side": "b", "type" : "p", "counter" : 0}, False] for file in range(8)]
rank_7 = [[(7, file), {"side": "b", "type": rk_7[file], "counter" : 0}, False] for file in range(8)]

'''
current_board is a list of ranks 0-7.

is_select will be a boolean deciding whether any piece is selected.

selected coords is a tuple declaring which coordinates are selected.
'''
current_board = [rank_0] + [rank_1] + ranks_2_5 + [rank_6] + [rank_7]
is_select = False
selected_coords = ""
