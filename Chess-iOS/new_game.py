rk_0 = 'RkbQKbkR'
rk_7 = 'RkbQKbkR'
empty = {"side": "n", "type": ""}

rank_0 = [[(0, file), {"side": "w", "type": rk_0[file], "counter" : 0}, False] for file in range(8)]
rank_1 = [[(1, file), {"side": "w", "type" : "p", "counter" : 0}, False] for file in range(8)]
ranks_2_5 = [[[(rank, file) , empty, False] for file in range(8)] for rank in range(2, 6)]
rank_6 = [[(6, file), {"side": "b", "type" : "p", "counter" : 0}, False] for file in range(8)]
rank_7 = [[(7, file), {"side": "b", "type": rk_7[file], "counter" : 0}, False] for file in range(8)]


current_board = [rank_0] + [rank_1] + ranks_2_5 + [rank_6] + [rank_7]
is_select = False
selected_coords = ""
