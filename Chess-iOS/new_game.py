rk_0 = 'RkbQKbkR'
rk_7 = 'RkbQKbkR'
rank_0 = [((rank, 0), {"side": "w", "type": rk_0[rank]}) for rank in range(8)]
rank_1 = [((rank, 1), {"side": "w", "type" : "p"}) for rank in range(8)]
ranks_2_5 = [((rank , file) , {"side": None, "type": ""}) for rank in range(8) for file in range(2, 6)]
rank_6 = [((rank, 6), {"side": "b", "type" : "p"}) for rank in range(8)]
rank_7 = [((rank, 7), {"side": "w", "type": rk_7[rank]}) for rank in range(8)]


new_game = rank_0 + rank_1 + ranks_2_5 + rank_6 + rank_7
