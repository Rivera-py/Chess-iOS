rk_0 = 'RkbQKbkR'
rk_7 = 'RkbQKbkR'
rank_0 = [[(0, file), {"side": "w", "type": rk_0[file]}, False] for file in range(8)]
rank_1 = [[(1, file), {"side": "w", "type" : "p"}, False] for file in range(8)]
ranks_2_5 = [[[(rank , file) , {"side": None, "type": ""}, False] for file in range(8)] for rank in range(2, 6)]
rank_6 = [[(6, file), {"side": "b", "type" : "p"}, False] for file in range(8)]
rank_7 = [[(7, file), {"side": "b", "type": rk_7[file]}, False] for file in range(8)]


current_board = [rank_0] + [rank_1] + ranks_2_5 + [rank_6] + [rank_7]

is_select = False
